use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
use pyo3::types::PyByteArray;

use skia_safe::{
    Color, ColorSpace, ColorType, Font, FontMgr, FontStyle, ImageInfo, Paint, PathBuilder,
    Point, RRect, Rect, TextBlob, Vector, surfaces,
};

fn create_skia_surface(width: i32, height: i32) -> PyResult<skia_safe::Surface> {
    let image_info = ImageInfo::new(
        (width, height),
        ColorType::BGRA8888,
        skia_safe::AlphaType::Premul,
        ColorSpace::new_srgb(),
    );
    let mut surface = surfaces::raster(&image_info, None, None)
        .ok_or_else(|| PyRuntimeError::new_err("Failed to create Skia raster surface"))?;
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
        ColorType::BGRA8888,
        skia_safe::AlphaType::Premul,
        ColorSpace::new_srgb(),
    );
    let mut surface = surfaces::wrap_pixels(&image_info, data, None, None)
        .ok_or_else(|| PyRuntimeError::new_err("Failed to create Skia raster surface"))?;
    surface.canvas().clear(Color::WHITE);
    Ok(surface.release())
}

#[pyclass(unsendable, module = "wyvern")]
struct Canvas {
    skia_surface: skia_safe::Surface,
    path: Option<skia_safe::PathBuilder>,
    font: Option<skia_safe::Font>,
}

#[pymethods]
impl Canvas {
    fn save(&mut self) {
        self.skia_surface.canvas().save();
    }

    fn restore(&mut self) {
        self.skia_surface.canvas().restore();
    }

    fn new_path(&mut self) {
        self.path = Some(PathBuilder::new());
    }

    fn move_to(&mut self, x: f32, y: f32) {
        self.path.get_or_insert_with(PathBuilder::new).move_to(Point::new(x, y));
    }

    fn line_to(&mut self, x: f32, y: f32) {
        self.path.get_or_insert_with(PathBuilder::new).line_to(Point::new(x, y));
    }

    fn rel_line_to(&mut self, x: f32, y: f32) -> PyResult<()> {
        self.path.as_mut()
            .ok_or_else(|| PyRuntimeError::new_err("Path does not exist for rel_line_to"))?
            .r_line_to(Vector::new(x, y));
        Ok(())
    }

    fn rel_curve_to(&mut self, x1: f32, y1: f32, x2: f32, y2: f32, x3: f32, y3: f32) -> PyResult<()> {
        self.path.as_mut()
            .ok_or_else(|| PyRuntimeError::new_err("Path does not exist for rel_curve_to"))?
            .r_cubic_to(Vector::new(x1, y1), Vector::new(x2, y2), Vector::new(x3, y3));
        Ok(())
    }

    fn rectangle(&mut self, left: f32, top: f32, width: f32, height: f32) {
        let r = Rect::new(left, top, left + width, top + height);
        self.path.get_or_insert_with(PathBuilder::new).add_rect(r, None, None);
    }

    fn round_rectangle(&mut self, left: f32, top: f32, width: f32, height: f32) {
        let r = Rect::new(left, top, left + width, top + height);
        self.path.get_or_insert_with(PathBuilder::new).add_rrect(RRect::new_rect(r), None, None);
    }

    fn close_path(&mut self) {
        if let Some(pb) = self.path.as_mut() {
            pb.close();
        }
    }

    fn set_source_rgba(&mut self, r: u8, g: u8, b: u8, a: u8) {
        let mut paint = Paint::default();
        paint.set_argb(a, r, g, b);
        self.skia_surface.canvas().draw_paint(&paint);
    }

    fn set_line_width(&mut self, width: f32) {
        let mut paint = Paint::default();
        paint.set_stroke_width(width);
        self.skia_surface.canvas().draw_paint(&paint);
    }

    fn select_font_face(&mut self, family_name: String) -> PyResult<()> {
        let typeface = FontMgr::new()
            .match_family_style(&family_name, FontStyle::normal())
            .ok_or_else(|| PyRuntimeError::new_err("Font family could not be found"))?;
        let size = self.font.as_ref().map(|f| f.size()).unwrap_or(12.0);
        self.font = Some(Font::from_typeface(typeface, size));
        Ok(())
    }

    fn set_font_size(&mut self, size: f32) -> PyResult<()> {
        let font = self.font.take().ok_or_else(|| {
            PyRuntimeError::new_err("Font face required for set_font_size")
        })?;
        self.font = Some(Font::from_typeface(font.typeface(), size));
        Ok(())
    }

    fn text_extents(&mut self, text: String) -> PyResult<(f32, f32, f32, f32, f32, f32)> {
        let font = self.font.as_ref().ok_or_else(|| {
            PyRuntimeError::new_err("Font face required for text_extents")
        })?;
        let blob = TextBlob::new(&text, font).ok_or_else(|| {
            PyRuntimeError::new_err("Issue with creating text blob for text_extents")
        })?;
        let b = blob.bounds();
        Ok((b.left(), b.top(), b.width(), b.height(), b.right(), b.bottom()))
    }

    fn text_path(&mut self, text: String) -> PyResult<()> {
        let font = self.font.as_ref().ok_or_else(|| {
            PyRuntimeError::new_err("Font face required for text_path")
        })?;
        let point = self.path.as_ref()
            .and_then(|pb| pb.snapshot().last_pt())
            .unwrap_or_else(|| Point::new(0.0, 0.0));
        self.skia_surface.canvas().draw_str(&text, point, font, &Paint::default());
        Ok(())
    }

    fn clip(&mut self) -> PyResult<()> {
        let path = self.path.take()
            .ok_or_else(|| PyRuntimeError::new_err("Path does not exist for clip"))?
            .detach();
        self.skia_surface.canvas().clip_path(&path, None, true);
        Ok(())
    }

    fn stroke(&mut self) -> PyResult<()> {
        let path = self.path.take()
            .ok_or_else(|| PyRuntimeError::new_err("Path does not exist for stroke"))?
            .detach();
        let mut paint = Paint::default();
        paint.set_stroke(true);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }

    fn fill(&mut self) -> PyResult<()> {
        let path = self.path.take()
            .ok_or_else(|| PyRuntimeError::new_err("Path does not exist for fill"))?
            .detach();
        let mut paint = Paint::default();
        paint.set_stroke(false);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }
}

// Module-level function wrappers so modal.py can use wyvern.save(ctx) style calls.
// Each wrapper borrows the canvas mutably, calls the method, then returns the same ctx.

#[pyfunction]
fn save(ctx: Py<Canvas>, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().save();
    ctx
}

#[pyfunction]
fn restore(ctx: Py<Canvas>, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().restore();
    ctx
}

#[pyfunction]
fn new_path(ctx: Py<Canvas>, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().new_path();
    ctx
}

#[pyfunction]
fn move_to(ctx: Py<Canvas>, x: f32, y: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().move_to(x, y);
    ctx
}

#[pyfunction]
fn line_to(ctx: Py<Canvas>, x: f32, y: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().line_to(x, y);
    ctx
}

#[pyfunction]
fn rel_line_to(ctx: Py<Canvas>, x: f32, y: f32, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().rel_line_to(x, y)?;
    Ok(ctx)
}

#[pyfunction]
fn rel_curve_to(ctx: Py<Canvas>, x1: f32, y1: f32, x2: f32, y2: f32, x3: f32, y3: f32, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().rel_curve_to(x1, y1, x2, y2, x3, y3)?;
    Ok(ctx)
}

#[pyfunction]
fn rectangle(ctx: Py<Canvas>, left: f32, top: f32, width: f32, height: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().rectangle(left, top, width, height);
    ctx
}

#[pyfunction]
fn round_rectangle(ctx: Py<Canvas>, left: f32, top: f32, width: f32, height: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().round_rectangle(left, top, width, height);
    ctx
}

#[pyfunction]
fn close_path(ctx: Py<Canvas>, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().close_path();
    ctx
}

#[pyfunction]
fn set_source_rgba(ctx: Py<Canvas>, r: u8, g: u8, b: u8, a: u8, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().set_source_rgba(r, g, b, a);
    ctx
}

#[pyfunction]
fn set_line_width(ctx: Py<Canvas>, width: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().set_line_width(width);
    ctx
}

#[pyfunction]
fn select_font_face(ctx: Py<Canvas>, family_name: String, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().select_font_face(family_name)?;
    Ok(ctx)
}

#[pyfunction]
fn set_font_size(ctx: Py<Canvas>, size: f32, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().set_font_size(size)?;
    Ok(ctx)
}

#[pyfunction]
fn text_path(ctx: Py<Canvas>, text: String, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().text_path(text)?;
    Ok(ctx)
}

#[pyfunction]
fn text_extents(ctx: Py<Canvas>, text: String, py: Python<'_>) -> PyResult<(f32, f32, f32, f32, f32, f32)> {
    ctx.bind(py).borrow_mut().text_extents(text)
}

#[pyfunction]
fn stroke(ctx: Py<Canvas>, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().stroke()?;
    Ok(ctx)
}

#[pyfunction]
fn clip(ctx: Py<Canvas>, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().clip()?;
    Ok(ctx)
}

#[pyfunction]
fn fill(ctx: Py<Canvas>, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().fill()?;
    Ok(ctx)
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
                    .ok_or_else(|| PyRuntimeError::new_err("Could not read pixel data from canvas"))?
                    .bytes()
                    .ok_or_else(|| PyRuntimeError::new_err("Could not read pixel data from canvas"))?,
            )
            .unbind();
            let canvas = Py::new(py, Canvas { skia_surface, path: None, font: None })?;
            Ok(ImageSurface { width, height, canvas, data })
        })
    }

    #[getter]
    fn width(&self) -> i32 { self.width }

    #[getter]
    fn height(&self) -> i32 { self.height }

    #[getter]
    fn canvas(&self, py: Python<'_>) -> Py<Canvas> {
        self.canvas.clone_ref(py)
    }

    #[getter]
    fn data(&self, py: Python<'_>) -> Py<PyByteArray> {
        self.data.clone_ref(py)
    }

    #[staticmethod]
    unsafe fn create_for_data(data: Bound<'_, PyByteArray>, width: i32, height: i32) -> PyResult<Self> {
        Python::attach(|py| {
            let mut skia_surface = create_surface_for_data(data.as_bytes_mut(), width, height)?;
            let data = PyByteArray::new(
                py,
                skia_surface
                    .peek_pixels()
                    .ok_or_else(|| PyRuntimeError::new_err("Could not read pixel data from canvas"))?
                    .bytes()
                    .ok_or_else(|| PyRuntimeError::new_err("Could not read pixel data from canvas"))?,
            )
            .unbind();
            let canvas = Py::new(py, Canvas { skia_surface, path: None, font: None })?;
            Ok(ImageSurface { width, height, canvas, data })
        })
    }
}

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
