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
use skia_safe::{surfaces, ColorType, ImageInfo, Color, ColorSpace, Paint};

#[pyclass(unsendable, module="wyvern")]
struct Canvas {
    skia_surface: skia_safe::Surface,
}

#[pymethods]
impl Canvas {
    fn draw_circle(&mut self, cx: f32, cy: f32, r: f32) {
        let canvas = self.skia_surface.canvas();
        let mut paint = Paint::default();
        paint.set_anti_alias(true);
        canvas.draw_circle((cx, cy), r, &paint);
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

fn create_skia_surface(width: i32, height: i32, scale_factor: f64) -> skia_safe::Surface {
    let image_info = ImageInfo::new(
        (width, height),
        ColorType::BGRA8888,
        skia_safe::AlphaType::Premul,
        ColorSpace::new_srgb(),
    );

    let mut surface = surfaces::raster(&image_info, None, None)
        .expect("Failed to create Skia raster surface");
    let scale = scale_factor as f32;
    surface.canvas().scale((scale, scale));
    surface.canvas().clear(Color::WHITE);
    surface
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

        let scale_factor = window.scale_factor();
        let (phys_width, phys_height) = {
            let size = window.inner_size();
            (size.width, size.height)
        };
        let logical_width = (phys_width as f64 / scale_factor) as u32;
        let logical_height = (phys_height as f64 / scale_factor) as u32;
        let skia_surface = create_skia_surface(phys_width as i32, phys_height as i32, scale_factor);

        Python::with_gil(|py| -> PyResult<()> {
            let py_canvas = Py::new(py, Canvas { skia_surface })?;
            let user_app = self.user_class.call1(py, (py_canvas.bind(py), logical_width, logical_height))?;

            self.py_canvas = Some(py_canvas);
            self.user_app = Some(user_app);
            Ok(())
        }).err().map(|err| {
            self.error = Some(err);
            event_loop.exit();
        });

        self.call_event_handler(event_loop, "init", ());

        self.internals = Some(AppInternals {
            window, softbuffer_surface
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
        } = app_internals;

        match event {
            WindowEvent::CloseRequested => { event_loop.exit(); }
            WindowEvent::Resized(new_size) => {
                let new_width = NonZero::new(new_size.width).unwrap();
                let new_height = NonZero::new(new_size.height).unwrap();
                softbuffer_surface.resize(new_width, new_height).expect("Failed to resize window buffer");

                let skia_surface = create_skia_surface(new_size.width as i32, new_size.height as i32, window.scale_factor());
                Python::with_gil(|py| {
                    let mut canvas_ref = py_canvas.borrow_mut(py);
                    canvas_ref.skia_surface = skia_surface;
                });
            }
            WindowEvent::CursorMoved { device_id: _, position } => {
                if self.last_mouse.elapsed() < Duration::from_millis(1000 / 60) {
                    return;
                }
                self.cursor_position = position;
                let scale = window.scale_factor();
                self.call_event_handler(event_loop, "mouse_moved", (position.x / scale, position.y / scale));
                self.last_mouse = Instant::now();
            }
            WindowEvent::MouseInput { device_id: _, state, button: _ } => {
                let scale = window.scale_factor();
                match state {
                    winit::event::ElementState::Pressed => {
                        self.call_event_handler(event_loop, "mouse_pressed", (self.cursor_position.x / scale, self.cursor_position.y / scale));
                    }
                    winit::event::ElementState::Released => {
                        self.call_event_handler(event_loop, "mouse_released", (self.cursor_position.x / scale, self.cursor_position.y / scale));
                    }
                }
            }
            WindowEvent::RedrawRequested => {
                let mut buffer = softbuffer_surface.buffer_mut().expect("Unable to access screen memory");
                Python::with_gil(|py| {
                    let mut canvas_ref = py_canvas.borrow_mut(py);
                    if let Some(pixmap) = canvas_ref.skia_surface.peek_pixels() {
                        if let Some(bytes) = pixmap.bytes() {
                            let pixels: &[u32] = unsafe {
                                std::slice::from_raw_parts(
                                    bytes.as_ptr() as *const u32,
                                    bytes.len() / 4,
                                )
                            };
                            buffer.copy_from_slice(pixels);
                        }
                    }
                });
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