// use pyo3::call::PyCallArgs;
use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
use pyo3::types::PyByteArray;
// use winit::dpi::PhysicalPosition;

// use std::any::Any;
// use std::num::NonZero;
// use std::rc::Rc;
// use std::time::{Duration, Instant};
// use winit::application::ApplicationHandler;
// use winit::event::WindowEvent;
// use winit::event_loop::{ActiveEventLoop, ControlFlow, EventLoop};
// use winit::window::{Window, WindowId};

use skia_safe::{Color, ColorSpace, ColorType, Font, FontMgr, FontStyle, ImageInfo, Paint, Path, PathBuilder, Point, RRect, Rect, Typeface, TextBlob, Vector, surfaces};

fn create_skia_surface(width: i32, height: i32) -> PyResult<skia_safe::Surface> {
    let image_info = ImageInfo::new(
        (width, height),
        // only one kind of format is used in Python code, but this can be made more modular
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
    surface.canvas().clear(Color::WHITE);
    Ok(surface)
}

unsafe fn create_surface_for_data(
    data: &mut [u8],
    width: i32,
    height: i32,
) -> PyResult<skia_safe::Surface> {
    let image_info = ImageInfo::new(
        (width, height),
        // only one kind of format is used in Python code, but this can be made more modular
        ColorType::BGRA8888,
        skia_safe::AlphaType::Premul,
        ColorSpace::new_srgb(),
    );

    let mut surface = match surfaces::wrap_pixels(&image_info, data, None, None) {
        Some(s) => s,
        None => {
            return Err(PyRuntimeError::new_err(
                "Failed to create Skia raster surface",
            ))
        }
    };
    surface.canvas().clear(Color::WHITE);
    Ok(surface.release())
}

#[pyclass(unsendable, module = "wyvern")]
#[derive(Clone)]
struct Canvas {
    skia_surface: skia_safe::Surface,
    path: Option<skia_safe::Path>,
    font: Option<skia_safe::Font>,
}

impl Canvas {
    fn save(mut self) -> PyResult<Self> {
        self.skia_surface.canvas().save();
        Ok(Canvas{ skia_surface: self.skia_surface, path: self.path, font: self.font })
    }

    fn restore(mut self) -> PyResult<Self> {
        self.skia_surface.canvas().restore();
        Ok(Canvas{ skia_surface: self.skia_surface, path: self.path, font: self.font })
    }

    fn new_path(self) -> PyResult<Self> {
        let path = Path::new();
        Ok(Canvas{ skia_surface: self.skia_surface, path: Some(path), font: self.font })
    }

    fn move_to(self, p : Point) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let mut path_builder = PathBuilder::new_path(path);
                let new_path = path_builder.move_to(p);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            },
            None => {
                let path = Path::new();
                let mut path_builder = PathBuilder::new_path(&path);
                let new_path = path_builder.move_to(p);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            }
        }
    }

    fn line_to(self, p : Point) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let mut path_builder = PathBuilder::new_path(path);
                let new_path = path_builder.line_to(p);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            },
            None => {
                let path = Path::new();
                let mut path_builder = PathBuilder::new_path(&path);
                let new_path = path_builder.line_to(p);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            }
        }
    }

    fn rel_line_to(self, v: Vector) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let mut path_builder = PathBuilder::new_path(path);
                let new_path = path_builder.r_line_to(v);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            },
            None => Err(PyRuntimeError::new_err("Path does not exist for rel_line_to"))
        }
    }

    fn rel_curve_to(self, p1: Vector, p2: Vector, p3: Vector) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let mut path_builder = PathBuilder::new_path(path);
                let new_path = path_builder.r_cubic_to(p1, p2, p3);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            },
            None => Err(PyRuntimeError::new_err("Path does not exist for rel_curve_to"))
        }
    }

    fn rectangle(self, r: Rect) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let mut path_builder = PathBuilder::new_path(path);
                let new_path = path_builder.add_rect(r, None, None);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            },
            None => {
                let path = Path::new();
                let mut path_builder = PathBuilder::new_path(&path);
                let new_path = path_builder.add_rect(r, None, None);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            }
        }
    }

    fn round_rectangle(self, r: RRect) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let mut path_builder = PathBuilder::new_path(path);
                let new_path = path_builder.add_rrect(r, None, None);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            },
            None => {
                let path = Path::new();
                let mut path_builder = PathBuilder::new_path(&path);
                let new_path = path_builder.add_rrect(r, None, None);
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            }
        }
    }

    fn close_path(self) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let mut path_builder = PathBuilder::new_path(path);
                let new_path = path_builder.close();
                Ok(Canvas { skia_surface: self.skia_surface, path: Some(new_path.detach()), font: self.font })
            },
            None => Ok(self)
        }
    }

    fn set_source_rgba(mut self, a: u8, r: u8, g: u8, b: u8) -> PyResult<Self> {
        let canvas = self.skia_surface.canvas();
        let mut paint = Paint::default();
        paint.set_argb(a, r, g, b);
        canvas.draw_paint(&paint);
        Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: self.font })
    }

    fn set_line_width(mut self, width: f32) -> PyResult<Self> {
        let canvas = self.skia_surface.canvas();
        let mut paint = Paint::default();
        paint.set_stroke_width(width);
        canvas.draw_paint(&paint);
        Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: self.font })
    }

    fn select_font_face(self, typeface: Typeface) -> PyResult<Self> {
        match &self.font {
            Some(font) => {
                let new_font = Font::from_typeface(typeface, font.size());
                Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: Some(new_font) })
            },
            None => {
                Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: Some(Font::from_typeface(typeface, None)) })
            }
        }
    }

    fn set_font_size(self, size: f32) -> PyResult<Self> {
        match &self.font {
            Some(font) => {
                let new_font = Font::from_typeface(font.typeface(), size);
                Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: Some(new_font) })
            },
            None => Err(PyRuntimeError::new_err("Font face required for set_font_size"))
        }
    }

    fn text_extents(&mut self, str: String) -> PyResult<(f32, f32, f32, f32, f32, f32)> {
        match &self.font {
            Some(font) => {
                let text_blob = TextBlob::new(str, font);
                match text_blob {
                    Some(blob) => {
                        let bounds = blob.bounds();
                        // may need to change this in case i misunderstood what these params are
                        Ok((bounds.left(), bounds.top(), bounds.width(), bounds.height(), bounds.right(), bounds.bottom()))
                    },
                    None => Err(PyRuntimeError::new_err("Issue with creating text blob for text_extents"))
                }
            },
            None => Err(PyRuntimeError::new_err("Font face required for text_extents"))
        }
    }

    fn text_path(mut self, str: String) -> PyResult<Self> {
        match &self.font {
            Some(font) => {
                let canvas = self.skia_surface.canvas();
                let paint = Paint::default();
                match &self.path {
                    Some(path) => {
                        match path.last_pt() {
                            Some(point) => {
                                canvas.draw_str(str, point, font, &paint);
                                Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: self.font })
                            },
                            None => {
                                canvas.draw_str(str, Point::new(0.0, 0.0), font, &paint);
                                Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: self.font })
                            }
                        }
                    },
                    None => {
                        canvas.draw_str(str, Point::new(0.0, 0.0), font, &paint);
                        Ok(Canvas { skia_surface: self.skia_surface, path: self.path, font: self.font })
                    }
                }
            },
            None => Err(PyRuntimeError::new_err("Font face required for text_path"))
        }
    }

    fn clip(mut self) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let canvas = self.skia_surface.canvas();
                canvas.clip_path(path, None, true);
                Ok(Canvas { skia_surface: self.skia_surface, path: None, font: self.font })
            },
            None => Err(PyRuntimeError::new_err("Path does not exist for clip"))
        }
    }

    fn stroke(mut self) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let canvas = self.skia_surface.canvas();
                let mut paint = Paint::default();
                paint.set_stroke(true);
                // not sure whether I need this
                paint.set_anti_alias(true);
                canvas.draw_path(path, &paint);
                Ok(Canvas { skia_surface: self.skia_surface, path: None, font: self.font })
            },
            None => Err(PyRuntimeError::new_err("Path does not exist for stroke"))
        }
    }

    // not sure about this
    fn fill(mut self) -> PyResult<Self> {
        match &self.path {
            Some(path) => {
                let canvas = self.skia_surface.canvas();
                let mut paint = Paint::default();
                paint.set_stroke(false);
                paint.set_anti_alias(true);
                canvas.draw_path(path, &paint);
                Ok(Canvas { skia_surface: self.skia_surface, path: None, font: self.font })
            },
            None => Err(PyRuntimeError::new_err("Path does not exist for stroke"))
        }
    }
}

// these are wrappers to work with the Py reference version of the Canvas, which is what is accessible in the Python code
#[pyfunction]
fn save(ctx: Py<Canvas>) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.save()?)
    })
}

#[pyfunction]
fn restore(ctx: Py<Canvas>) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.restore()?)
    })
}

#[pyfunction]
fn new_path(ctx: Py<Canvas>) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.new_path()?)
    })
}

#[pyfunction]
fn move_to(ctx: Py<Canvas>, x: f32, y: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        let point = Point::new(x, y);
        Py::new(py, ctx.extract::<Canvas>(py)?.move_to(point)?)
    })
}

#[pyfunction]
fn line_to(ctx: Py<Canvas>, x: f32, y: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        let point = Point::new(x, y);
        Py::new(py, ctx.extract::<Canvas>(py)?.line_to(point)?)
    })
}

#[pyfunction]
fn rel_line_to(ctx: Py<Canvas>, x: f32, y: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        let vector = Vector::new(x, y);
        Py::new(py, ctx.extract::<Canvas>(py)?.rel_line_to(vector)?)
    })
}

#[pyfunction]
fn rel_curve_to(ctx: Py<Canvas>, x1: f32, y1: f32, x2: f32, y2: f32, x3: f32, y3: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        let p1 = Vector::new(x1, y1);
        let p2 = Vector::new(x2, y2);
        let p3 = Vector::new(x3, y3);
        Py::new(py, ctx.extract::<Canvas>(py)?.rel_curve_to(p1, p2, p3)?)
    })
}

#[pyfunction]
fn rectangle(ctx: Py<Canvas>, left: f32, top: f32, width: f32, height: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        let r = Rect::new(left, top, left + width, top + height);
        Py::new(py, ctx.extract::<Canvas>(py)?.rectangle(r)?)
    })
}

#[pyfunction]
fn round_rectangle(ctx: Py<Canvas>, left: f32, top: f32, width: f32, height: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        let r = Rect::new(left, top, left + width, top + height);
        let rr = RRect::new_rect(r);
        Py::new(py, ctx.extract::<Canvas>(py)?.round_rectangle(rr)?)
    })
}

#[pyfunction]
fn close_path(ctx: Py<Canvas>) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.close_path()?)
    })
}

#[pyfunction]
fn set_source_rgba(ctx: Py<Canvas>, r: u8, g: u8, b: u8, a: u8) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.set_source_rgba(a, r, g, b)?)
    })
}

#[pyfunction]
fn set_line_width(ctx: Py<Canvas>, width: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.set_line_width(width)?)
    })
}

#[pyfunction]
fn select_font_face(ctx: Py<Canvas>, family_name: String) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        let font_mgr = FontMgr::new();
        // making it just normal for now, maybe can modulate it in the future
        match font_mgr.match_family_style(family_name, FontStyle::normal()) {
            Some(typeface) => Py::new(py, ctx.extract::<Canvas>(py)?.select_font_face(typeface)?),
            None => Err(PyRuntimeError::new_err("Font family could not be found"))
        }
    })
}

#[pyfunction]
fn set_font_size(ctx: Py<Canvas>, size: f32) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.set_font_size(size)?)
    })
}

#[pyfunction]
fn text_path(ctx: Py<Canvas>, str: String) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.text_path(str)?)
    })
}

#[pyfunction]
fn text_extents(ctx: Py<Canvas>, str: String) -> PyResult<(f32, f32, f32, f32, f32, f32)> {
    Python::attach(|py| {
        ctx.extract::<Canvas>(py)?.text_extents(str)
    })
}

#[pyfunction]
fn stroke(ctx: Py<Canvas>) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.stroke()?)
    })
}

#[pyfunction]
fn clip(ctx: Py<Canvas>) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.clip()?)
    })
}

#[pyfunction]
fn fill(ctx: Py<Canvas>) -> PyResult<Py<Canvas>> {
    Python::attach(|py| {
        Py::new(py, ctx.extract::<Canvas>(py)?.fill()?)
    })
}

#[pyclass(module = "wyvern", subclass)]
struct ImageSurface {
    width: i32,
    height: i32,
    canvas: Py<Canvas>,
    data: Py<PyByteArray>,
}

#[pymethods]
impl ImageSurface {
    #[new]
    fn create(width: i32, height: i32) -> PyResult<Self> {
        Python::attach(|py| {
            let mut skia_surface = create_skia_surface(width, height)?;
            let data = PyByteArray::new(
                py,
                skia_surface
                    .peek_pixels()
                    .ok_or(PyRuntimeError::new_err(
                        "Could not read pixel data from canvas",
                    ))?
                    .bytes()
                    .ok_or(PyRuntimeError::new_err(
                        "Could not read pixel data from canvas",
                    ))?,
            )
            .unbind();
            let canvas = Py::new(py, Canvas { skia_surface, path: None, font: None })?;
            Ok(ImageSurface {
                width,
                height,
                canvas,
                data,
            })
        })
    }

    #[getter]
    fn width(&self) -> PyResult<i32> {
        Ok(self.width)
    }

    #[getter]
    fn height(&self) -> PyResult<i32> {
        Ok(self.height)
    }

    #[getter]
    fn canvas(&self) -> PyResult<Py<Canvas>> {
        Python::attach(|py| -> PyResult<Py<Canvas>> { Ok(self.canvas.clone_ref(py)) })
    }

    #[getter]
    fn data(&self) -> PyResult<Py<PyByteArray>> {
        Python::attach(|py| Ok(self.data.clone_ref(py)))
    }

    #[staticmethod]
    unsafe fn create_for_data(
        data: Bound<'_, PyByteArray>,
        width: i32,
        height: i32,
    ) -> PyResult<Self> {
        Python::attach(|py| {
            let mut skia_surface = create_surface_for_data(data.as_bytes_mut(), width, height)?;
            let data = PyByteArray::new(
                py,
                skia_surface
                    .peek_pixels()
                    .ok_or(PyRuntimeError::new_err(
                        "Could not read pixel data from canvas",
                    ))?
                    .bytes()
                    .ok_or(PyRuntimeError::new_err(
                        "Could not read pixel data from canvas",
                    ))?,
            )
            .unbind();
            let canvas = Py::new(py, Canvas { skia_surface, path: None, font: None })?;
            Ok(ImageSurface {
                width,
                height,
                canvas,
                data,
            })
        })
    }
}

// #[pyclass(unsendable, module = "wyvern")]
// struct Time {
//     init_tick: Instant,
// }

// impl Time {
//     fn new() -> Self {
//         Time { init_tick: Instant::now() }
//     }

//     fn get_ticks(&mut self) -> u128 {
//         Instant::elapsed(&self.init_tick).as_millis()
//     }
// }

// #[pyclass(module = "wyvern", subclass)]
// struct Game {
//     time: Py<Time>,
// }

// impl Game {
//     fn init() -> PyResult<Self> {
//         Python::attach(|py| {
//             let time = Py::new(py, Time::new())?;
//             Ok(Game { time })
//         })
//     }
// }

#[pymodule]
fn wyvern(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<ImageSurface>()?;
    m.add_function(wrap_pyfunction!(save, m)?)?;
    m.add_function(wrap_pyfunction!(restore, m)?)?;
    m.add_function(wrap_pyfunction!(new_path, m)?)?;
    m.add_function(wrap_pyfunction!(move_to, m)?)?;
    m.add_function(wrap_pyfunction!(line_to, m)?)?;
    m.add_function(wrap_pyfunction!(rel_line_to, m)?)?;
    m.add_function(wrap_pyfunction!(rel_curve_to, m)?)?;
    m.add_function(wrap_pyfunction!(rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(round_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(close_path, m)?)?;
    m.add_function(wrap_pyfunction!(set_source_rgba, m)?)?;
    m.add_function(wrap_pyfunction!(set_line_width, m)?)?;
    m.add_function(wrap_pyfunction!(select_font_face, m)?)?;
    m.add_function(wrap_pyfunction!(set_font_size, m)?)?;
    m.add_function(wrap_pyfunction!(text_path, m)?)?;
    m.add_function(wrap_pyfunction!(text_extents, m)?)?;
    m.add_function(wrap_pyfunction!(stroke, m)?)?;
    m.add_function(wrap_pyfunction!(clip, m)?)?;
    m.add_function(wrap_pyfunction!(fill, m)?)?;
    Ok(())
}
