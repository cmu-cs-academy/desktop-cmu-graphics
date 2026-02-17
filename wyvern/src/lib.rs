use pyo3::call::PyCallArgs;
use pyo3::prelude::*;
use winit::dpi::PhysicalPosition;

use std::num::NonZero;
use std::rc::Rc;
use std::time::{Duration, Instant};
use winit::application::ApplicationHandler;
use winit::event::WindowEvent;
use winit::event_loop::{ActiveEventLoop, ControlFlow, EventLoop};
use winit::window::{Window, WindowId};

use softbuffer;
use skia_safe::{surfaces, ImageInfo, Color, ColorSpace, Paint};

#[pyclass(unsendable, module="wyvern")]
struct Canvas {
    skia_surface: skia_safe::Surface,
}

#[pymethods]
impl Canvas {
    fn draw_circle(&mut self, cx: f32, cy: f32, r: f32) {
        let canvas = self.skia_surface.canvas();
        canvas.draw_circle((cx, cy), r, &Paint::default());
    }

    fn clear(&mut self) {
        let canvas = self.skia_surface.canvas();
        canvas.clear(Color::WHITE);
    }
}


#[pyclass(module="wyvern", subclass)]
struct App {
    width: u32,
    height: u32,
    canvas: Py<Canvas>,
}

#[pymethods]
impl App {
    #[new]
    fn new(canvas: Py<Canvas>, width: u32, height: u32) -> Self {
        App {canvas, width, height}
    }

    #[getter]
    fn width(&self) -> PyResult<u32> {
        Ok(self.width)
    }

    #[getter]
    fn height(&self) -> PyResult<u32> {
        Ok(self.height)
    }

    #[getter]
    fn canvas(&self) -> PyResult<Py<Canvas>> {
        Python::with_gil(|py| -> PyResult<Py<Canvas>> {
            Ok(self.canvas.clone_ref(py))
        })
    }
}

struct AppInternals {
    window: Rc<Window>,
    softbuffer_surface: softbuffer::Surface<Rc<Window>, Rc<Window>>,
    skia_buffer: Vec<u32>,
}

struct WinitApp {
    internals: Option<AppInternals>,
    last_tick: Instant,
    last_mouse: Instant,
    cursor_position: PhysicalPosition<f64>,
    py_canvas: Option<Py<Canvas>>,
    user_app: Option<Py<PyAny>>,
    user_class: Py<PyAny>,
    error: Option<PyErr>,
}

fn get_skia_surface_and_buffer(window: &Window) -> (skia_safe::Surface, Vec<u32>) {
    let (width, height) = {
        let size = window.inner_size();
        (size.width as i32, size.height as i32)
    };
    let mut skia_buffer: Vec<u32> = vec![0; (width * height).try_into().expect("Screen is too large")];

    let image_info = {
        let color_space = ColorSpace::new_srgb();
        ImageInfo::new_n32(
            (width, height),
            skia_safe::AlphaType::Premul,
            color_space,
        )
    };

    let pixel_bytes: &mut [u8] = unsafe {
        std::slice::from_raw_parts_mut(
            skia_buffer.as_mut_ptr() as *mut u8,
            skia_buffer.len() * std::mem::size_of::<u32>(),
        )
    };

    let mut skia_surface = surfaces::wrap_pixels(
        &image_info,
        pixel_bytes,
        (width * 4) as usize,
        None,
    )
    .unwrap();
    skia_surface.canvas().clear(Color::WHITE);

    (skia_surface.clone(), skia_buffer)
}

impl WinitApp {
    fn call_event_handler<A>(&mut self, event_loop: &ActiveEventLoop, handler_name: &str, args: A)
    where
        A: for<'py> PyCallArgs<'py>,
    {
        let user_app = match self.user_app.as_ref() {
            Some(user_app) => user_app,
            None => return
        };

        let handler_result = Python::with_gil(|py| -> PyResult<()> {
            let bound_app = user_app.bind(py);

            if bound_app.hasattr(handler_name)? {
                let handler = bound_app.getattr(handler_name)?;
                handler.call1(args)?;
            }

            Ok(())
        });

        if let Some(err) = handler_result.err() {
            self.error = Some(err);
            event_loop.exit();
        } else {
            if let Some(internals) = self.internals.as_ref() {
                internals.window.request_redraw();
            }
        }
    }
}

impl ApplicationHandler for WinitApp {
    fn resumed(&mut self, event_loop: &ActiveEventLoop) {
        let window = Rc::new(
            event_loop
                .create_window(Window::default_attributes())
                .unwrap(),
        );
        let softbuffer_surface = {
            let context = softbuffer::Context::new(window.clone()).unwrap();
            softbuffer::Surface::new(&context, window.clone()).unwrap()
        };

        let (skia_surface, skia_buffer) =  get_skia_surface_and_buffer(&window);

        Python::with_gil(|py| -> PyResult<()> {
            let (width, height) = {
                let size = window.inner_size();
                (size.width, size.height)
            };

            let py_canvas = Py::new(py, Canvas { skia_surface: skia_surface.clone() })?;
            let user_app = self.user_class.call1(py, (py_canvas.bind(py), width, height))?;

            self.py_canvas = Some(py_canvas);
            self.user_app = Some(user_app);
            Ok(())
        }).err().map(|err| {
            self.error = Some(err);
            event_loop.exit();
        });

        self.call_event_handler(event_loop, "init", ());

        self.internals = Some(AppInternals {
            window, softbuffer_surface, skia_buffer
        });

    }

    fn about_to_wait(&mut self, event_loop: &ActiveEventLoop) {
        let fps = 60;
        let elapsed = self.last_tick.elapsed();
        if elapsed >= Duration::from_millis(1000 / fps) {
            let py_seconds = (elapsed.as_millis() as f64) / 1000.0;
            self.call_event_handler(event_loop, "tick", (py_seconds,));
            self.last_tick = Instant::now();
        }
    }

    fn window_event(&mut self, event_loop: &ActiveEventLoop, _id: WindowId, event: WindowEvent) {
        let app_internals = match self.internals.as_mut() {
            Some(app_internals) => app_internals,
            None => return
        };
        let py_canvas = match self.py_canvas.as_mut() {
            Some(py_canvas) => py_canvas,
            None => return
        };

        let AppInternals {
            window,
            softbuffer_surface,
            skia_buffer
        } = app_internals;

        match event {
            WindowEvent::CloseRequested => { event_loop.exit(); }
            WindowEvent::Resized(new_size) => {
                let new_width = NonZero::new(new_size.width).unwrap();
                let new_height = NonZero::new(new_size.height).unwrap();
                softbuffer_surface.resize(new_width, new_height).expect("Failed to resize window buffer");

                let (skia_surface, skia_buffer) = get_skia_surface_and_buffer(&window);
                Python::with_gil(|py| {
                    let mut canvas_ref = py_canvas.borrow_mut(py);
                    canvas_ref.skia_surface = skia_surface;
                });
                app_internals.skia_buffer = skia_buffer;
            }
            WindowEvent::CursorMoved { device_id: _, position } => {
                if self.last_mouse.elapsed() < Duration::from_millis(1000 / 60) {
                    return;
                }
                self.cursor_position = position;
                self.call_event_handler(event_loop, "mouse_moved", (position.x, position.y));
                self.last_mouse = Instant::now();
            }
            WindowEvent::MouseInput { device_id: _, state, button: _ } => {
                match state {
                    winit::event::ElementState::Pressed => {
                        self.call_event_handler(event_loop, "mouse_pressed", (self.cursor_position.x, self.cursor_position.y));
                    }
                    winit::event::ElementState::Released => {
                        self.call_event_handler(event_loop, "mouse_released", (self.cursor_position.x, self.cursor_position.y));
                    }
                }
            }
            WindowEvent::RedrawRequested => {
                let mut buffer = softbuffer_surface.buffer_mut().expect("Unable to access screen memory");
                buffer.copy_from_slice(&skia_buffer);
                buffer.present().expect("Error drawing to the screen");
            }
            WindowEvent::KeyboardInput { device_id: _, event, is_synthetic: _, } => {
                if let Some(key) = event.logical_key.to_text() {
                    match event.state {
                        winit::event::ElementState::Pressed => {
                            self.call_event_handler(event_loop, "key_pressed", (key,));
                        }
                        winit::event::ElementState::Released => {
                            self.call_event_handler(event_loop, "key_released", (key,));
                        }
                    }
                }
            }
            _ => (),
        }
    }
}

#[pyfunction]
fn run(user_class: Py<PyAny>) -> PyResult<()> {
    let mut app = WinitApp{
        internals: None,
        last_tick: Instant::now(),
        last_mouse: Instant::now(),
        cursor_position: PhysicalPosition {x: 0.0, y: 0.0},
        py_canvas: None,
        user_class,
        user_app: None,
        error: None,
    };

    let event_loop = EventLoop::new().expect("Unable to start event loop");
    event_loop.set_control_flow(ControlFlow::Poll);
    let _ = event_loop.run_app(&mut app);

    match app.error {
        None => Ok(()),
        Some(err) => Err(err)
    }
}

#[pymodule]
fn wyvern(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<App>()?;
    m.add_function(wrap_pyfunction!(run, m)?)?;
    Ok(())
}