use pyo3::call::PyCallArgs;
use pyo3::exceptions::{PyOSError, PyRuntimeError};
use pyo3::prelude::*;
use winit::dpi::PhysicalPosition;

use std::num::NonZero;
use std::rc::Rc;
use std::time::{Duration, Instant};
use winit::application::ApplicationHandler;
use winit::event::WindowEvent;
use winit::event_loop::{ActiveEventLoop, ControlFlow, EventLoop};
use winit::window::{Window, WindowId};

use skia_safe::{surfaces, Color, ColorSpace, ColorType, ImageInfo, Paint};

#[pyclass(unsendable, module = "wyvern")]
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

#[pyclass(module = "wyvern", subclass)]
struct App {
    width: u32,
    height: u32,
    canvas: Py<Canvas>,
}

#[pymethods]
impl App {
    #[new]
    fn new(canvas: Py<Canvas>, width: u32, height: u32) -> Self {
        App {
            canvas,
            width,
            height,
        }
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
        Python::attach(|py| -> PyResult<Py<Canvas>> { Ok(self.canvas.clone_ref(py)) })
    }
}

/* cmu_graphics Apps methods that depend on pygame/cairo
  - getScreenshot
  - translateEventHandlerArgs(?)
  - getEventHanderArgs(?)
  - callUserFn(?)
  - redrawAllWrapper(?)
  - getKey
  - drawErrorScreen
  - getModifiers
  - handleKeyPress
  - handleKeyRelease*
  - redrawAll
  - updateScreen
  - run
*/

struct AppInternals {
    window: Option<Rc<Window>>,
    softbuffer_surface: Option<softbuffer::Surface<Rc<Window>, Rc<Window>>>,
    error: Option<PyErr>,
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

fn create_skia_surface(
    width: i32,
    height: i32,
    scale_factor: f64,
) -> Result<skia_safe::Surface, PyErr> {
    let image_info = ImageInfo::new(
        (width, height),
        ColorType::BGRA8888,
        skia_safe::AlphaType::Premul,
        ColorSpace::new_srgb(),
    );

    let mut surface = match surfaces::raster(&image_info, None, None) {
        Some(s) => s,
        None => {
            return Err(PyRuntimeError::new_err(
                "Failed to create Skia raster surface",
            ))
        }
    };
    let scale = scale_factor as f32;
    surface.canvas().scale((scale, scale));
    surface.canvas().clear(Color::WHITE);
    Ok(surface)
}

impl WinitApp {
    fn call_event_handler<A>(&mut self, event_loop: &ActiveEventLoop, handler_name: &str, args: A)
    where
        A: for<'py> PyCallArgs<'py>,
    {
        let user_app = match self.user_app.as_ref() {
            Some(user_app) => user_app,
            None => return,
        };

        let handler_result = Python::attach(|py| -> PyResult<()> {
            let bound_app = user_app.bind(py);

            if bound_app.hasattr(handler_name)? {
                let handler = bound_app.getattr(handler_name)?;
                handler.call1(args)?;
            }

            match &self.internals {
                Some(internals) => match &internals.error {
                    Some(err) => Err(err.clone_ref(py)),
                    None => Ok(()),
                },
                None => Ok(()),
            }
        });

        match handler_result.err() {
            Some(err) => {
                self.error = Some(err);
                event_loop.exit();
            }
            None => {
                if let Some(internals) = &self.internals {
                    match &internals.window {
                        Some(window) => window.request_redraw(),
                        None => {
                            self.error = Some(PyOSError::new_err("Unable to create winit window"));
                            event_loop.exit()
                        }
                    }
                }
            }
        }
    }
}

impl ApplicationHandler for WinitApp {
    fn resumed(&mut self, event_loop: &ActiveEventLoop) {
        let window = match event_loop.create_window(Window::default_attributes()) {
            Ok(window) => Rc::new(window),
            Err(_) => {
                let pyerr = PyOSError::new_err("Unable to create winit window");
                self.internals = Some(AppInternals {
                    window: None,
                    softbuffer_surface: None,
                    error: Some(pyerr),
                });
                return;
            }
        };
        let softbuffer_surface = {
            let context = softbuffer::Context::new(window.clone());
            match context {
                Ok(context) => softbuffer::Surface::new(&context, window.clone())
                    .map_err(|_| PyOSError::new_err("Issue with creating softbuffer surface")),
                Err(_) => Err(PyOSError::new_err("Issue with creating softbuffer context")),
            }
        };

        let scale_factor = window.scale_factor();
        let (phys_width, phys_height) = {
            let size = window.inner_size();
            (size.width, size.height)
        };
        let logical_width = (phys_width as f64 / scale_factor) as u32;
        let logical_height = (phys_height as f64 / scale_factor) as u32;
        let skia_surface = create_skia_surface(phys_width as i32, phys_height as i32, scale_factor);

        if let Some(err) = Python::attach(|py| -> PyResult<()> {
            let py_canvas = match skia_surface {
                Ok(skia_surface) => Py::new(py, Canvas { skia_surface })?,
                Err(pyerr) => return Err(pyerr),
            };
            let user_app = self
                .user_class
                .call1(py, (py_canvas.bind(py), logical_width, logical_height))?;

            self.py_canvas = Some(py_canvas);
            self.user_app = Some(user_app);
            Ok(())
        })
        .err()
        {
            self.error = Some(err);
            event_loop.exit();
        };

        self.call_event_handler(event_loop, "init", ());

        match softbuffer_surface {
            Ok(softbuffer_surface) => {
                self.internals = Some(AppInternals {
                    window: Some(window),
                    softbuffer_surface: Some(softbuffer_surface),
                    error: None,
                })
            }
            Err(pyerr) => {
                self.internals = Some(AppInternals {
                    window: Some(window),
                    softbuffer_surface: None,
                    error: Some(pyerr),
                })
            }
        }
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
            None => return,
        };
        let py_canvas = match self.py_canvas.as_mut() {
            Some(py_canvas) => py_canvas,
            None => return,
        };

        let AppInternals {
            window,
            softbuffer_surface,
            error: _,
        } = app_internals;

        match event {
            WindowEvent::CloseRequested => {
                event_loop.exit();
            }
            WindowEvent::Resized(new_size) => {
                let new_width = match NonZero::new(new_size.width) {
                    Some(new_width) => new_width,
                    None => {
                        self.error =
                            Some(PyOSError::new_err("Issue with resizing width of canvas"));
                        event_loop.exit();
                        return;
                    }
                };
                let new_height = match NonZero::new(new_size.height) {
                    Some(new_height) => new_height,
                    None => {
                        self.error =
                            Some(PyOSError::new_err("Issue with resizing height of canvas"));
                        event_loop.exit();
                        return;
                    }
                };
                match softbuffer_surface {
                    Some(softbuffer_surface) => match softbuffer_surface
                        .resize(new_width, new_height)
                    {
                        Ok(()) => (),
                        Err(_) => {
                            self.error = Some(PyOSError::new_err("Failed to resize window buffer"));
                            event_loop.exit()
                        }
                    },
                    None => {
                        self.error =
                            Some(PyOSError::new_err("Issue with creation of window buffer"));
                        event_loop.exit()
                    }
                }

                let skia_surface = match window {
                    Some(window) => create_skia_surface(
                        new_size.width as i32,
                        new_size.height as i32,
                        window.scale_factor(),
                    ),
                    None => Err(PyOSError::new_err("Unable to create winit window")),
                };
                Python::attach(|py| {
                    match skia_surface {
                        Ok(skia_surface) => {
                            let mut canvas_ref = py_canvas.borrow_mut(py);
                            canvas_ref.skia_surface = skia_surface
                        }
                        // would it be better for this to error out/panic in some way?
                        Err(err) => {
                            self.error = Some(err);
                            event_loop.exit()
                        }
                    }
                });
            }
            WindowEvent::CursorMoved {
                device_id: _,
                position,
            } => {
                if self.last_mouse.elapsed() < Duration::from_millis(1000 / 60) {
                    return;
                }
                self.cursor_position = position;
                let scale = match window {
                    Some(window) => Ok(window.scale_factor()),
                    None => Err(PyOSError::new_err("Unable to create winit window")),
                };
                match scale {
                    Ok(scale) => {
                        self.call_event_handler(
                            event_loop,
                            "mouse_moved",
                            (position.x / scale, position.y / scale),
                        );
                        self.last_mouse = Instant::now();
                    }
                    Err(err) => {
                        self.error = Some(err);
                        event_loop.exit()
                    }
                }
            }
            WindowEvent::MouseInput {
                device_id: _,
                state,
                button: _,
            } => {
                let scale = match window {
                    Some(window) => Ok(window.scale_factor()),
                    None => Err(PyOSError::new_err("Unable to create winit window")),
                };
                match scale {
                    Ok(scale) => match state {
                        winit::event::ElementState::Pressed => {
                            self.call_event_handler(
                                event_loop,
                                "mouse_pressed",
                                (
                                    self.cursor_position.x / scale,
                                    self.cursor_position.y / scale,
                                ),
                            );
                        }
                        winit::event::ElementState::Released => {
                            self.call_event_handler(
                                event_loop,
                                "mouse_released",
                                (
                                    self.cursor_position.x / scale,
                                    self.cursor_position.y / scale,
                                ),
                            );
                        }
                    },
                    Err(err) => {
                        self.error = Some(err);
                        event_loop.exit()
                    }
                }
            }
            WindowEvent::RedrawRequested => {
                let mut buffer = match softbuffer_surface {
                    Some(softbuffer_surface) => softbuffer_surface
                        .buffer_mut()
                        .map_err(|_| PyOSError::new_err("Issue with creation of window buffer")),
                    None => Err(PyOSError::new_err("Failed to resize window buffer")),
                };
                Python::attach(|py| {
                    let mut canvas_ref = py_canvas.borrow_mut(py);
                    if let Some(pixmap) = canvas_ref.skia_surface.peek_pixels() {
                        if let Some(bytes) = pixmap.bytes() {
                            let pixels: &[u32] = unsafe {
                                std::slice::from_raw_parts(
                                    bytes.as_ptr() as *const u32,
                                    bytes.len() / 4,
                                )
                            };
                            let _ = buffer.as_mut().map(|b| b.copy_from_slice(pixels));
                        }
                        let buffer_error = PyOSError::new_err("Error drawing to the screen");
                        match buffer {
                            Ok(b) => match b.present() {
                                Ok(()) => (),
                                Err(_) => {
                                    self.error = Some(buffer_error);
                                    event_loop.exit()
                                }
                            },
                            Err(_) => {
                                self.error = Some(buffer_error);
                                event_loop.exit()
                            }
                        }
                    }
                });
            }
            WindowEvent::KeyboardInput {
                device_id: _,
                event,
                is_synthetic: _,
            } => {
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
    let mut app = WinitApp {
        internals: None,
        last_tick: Instant::now(),
        last_mouse: Instant::now(),
        cursor_position: PhysicalPosition { x: 0.0, y: 0.0 },
        py_canvas: None,
        user_class,
        user_app: None,
        error: None,
    };

    let event_loop = match EventLoop::new() {
        Ok(event_loop) => event_loop,
        Err(_) => return Err(PyOSError::new_err("Unable to start event loop")),
    };
    event_loop.set_control_flow(ControlFlow::Poll);
    let _ = event_loop.run_app(&mut app);

    match app.error {
        None => Ok(()),
        Some(err) => Err(err),
    }
}

#[pymodule]
fn wyvern(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<App>()?;
    m.add_function(wrap_pyfunction!(run, m)?)?;
    Ok(())
}
