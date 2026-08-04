/* PYGEO */
use pyo3::Bound;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyModule;

use geo::BooleanOps;
use geo::{LineString, MultiPolygon, Polygon};

// type aliases
type PyLineString = Vec<(f64, f64)>;
type PyPolygon = Vec<PyLineString>;
type PyMultiPolygon = Vec<PyPolygon>;

// conversions from Python to Rust
fn py_polygon_to_polygon(poly: PyPolygon) -> Polygon<f64> {
    let mut line_strings = poly.into_iter().map(LineString::from);

    match line_strings.next() {
        Some(exterior) => Polygon::new(exterior, line_strings.collect()),
        None => Polygon::empty(),
    }
}

fn py_multi_polygon_to_multi_polygon(multi_poly: PyMultiPolygon) -> MultiPolygon<f64> {
    let polys = multi_poly.into_iter().map(py_polygon_to_polygon).collect();
    MultiPolygon::new(polys)
}

// conversions from Rust to Python
fn line_string_to_vec(line_string: &LineString<f64>) -> PyLineString {
    line_string.points().map(|p| (p.x(), p.y())).collect()
}

fn polygon_to_py_polygon(poly: Polygon<f64>) -> PyPolygon {
    let holes = poly.interiors().iter().map(line_string_to_vec);
    let exterior = line_string_to_vec(poly.exterior());

    std::iter::once(exterior).chain(holes).collect()
}

fn multi_polygon_to_py_multi_polygon(multi_poly: MultiPolygon<f64>) -> PyMultiPolygon {
    multi_poly.into_iter().map(polygon_to_py_polygon).collect()
}

// Unions a vector of PyMultiPolygons
#[pyfunction]
fn union(py_polys: Vec<PyMultiPolygon>) -> PyResult<PyMultiPolygon> {
    let union_result_or_none = py_polys
        .into_iter()
        .map(py_multi_polygon_to_multi_polygon)
        .reduce(|u, m| m.union(&u));

    match union_result_or_none {
        Some(union_result) => Ok(multi_polygon_to_py_multi_polygon(union_result)),
        None => Err(PyValueError::new_err(
            "union must be given at least one MultiPolygon as input",
        )),
    }
}
/* PYGEO */

/* WYVERN */
use std::f32::consts::PI;

use pyo3::exceptions::PyRuntimeError;
use pyo3::types::PyByteArray;

use skia_safe::{
    Color, Color4f, ColorSpace, ColorType, Font, FontMgr, FontStyle, Image, ImageInfo, Matrix,
    Paint, PaintJoin, Path, PathBuilder, PathEffect, Point, RRect, Rect, TileMode, Typeface,
    Vector, font_style, gradient, surfaces,
};

const RAD_TO_DEG: f32 = 180.0 / PI;
const ORIGIN: Point = Point::new(0.0, 0.0);

fn create_skia_surface(width: i32, height: i32, scale_factor: f64) -> PyResult<skia_safe::Surface> {
    let width = width.max(1);
    let height = height.max(1);
    let image_info = ImageInfo::new(
        (width, height),
        ColorType::BGRA8888,
        skia_safe::AlphaType::Premul,
        ColorSpace::new_srgb(),
    );
    let mut surface = surfaces::raster(&image_info, None, None)
        .ok_or_else(|| PyRuntimeError::new_err("Failed to create Skia raster surface"))?;
    let scale = scale_factor as f32;
    surface.canvas().scale((scale, scale));
    surface.canvas().clear(Color::WHITE);
    Ok(surface)
}

fn new_path_and_move(p: Point) -> PathBuilder {
    let mut new_path = PathBuilder::new();
    new_path.move_to(p);
    new_path
}

fn new_path_and_line(p: Point) -> PathBuilder {
    let mut new_path = PathBuilder::new();
    new_path.line_to(p);
    new_path
}

#[pyclass(from_py_object)]
#[derive(Clone)]
enum LineJoin {
    MITER,
    ROUND,
    BEVEL,
}

#[pyclass(from_py_object)]
#[derive(Clone)]
enum FontWeight {
    BOLD,
    NORMAL,
}

fn py_to_skia_weight(weight: FontWeight) -> font_style::Weight {
    match weight {
        FontWeight::BOLD => font_style::Weight::BOLD,
        FontWeight::NORMAL => font_style::Weight::NORMAL,
    }
}

#[pyclass(from_py_object)]
#[derive(Clone)]
enum FontSlant {
    ITALIC,
    NORMAL,
    OBLIQUE,
}

fn py_to_skia_slant(slant: FontSlant) -> font_style::Slant {
    match slant {
        FontSlant::ITALIC => font_style::Slant::Italic,
        FontSlant::NORMAL => font_style::Slant::Upright,
        FontSlant::OBLIQUE => font_style::Slant::Oblique,
    }
}

fn get_arial(font_mgr: &FontMgr, style: FontStyle) -> PyResult<Typeface> {
    let arial = font_mgr
        .match_family_style("Arial", style)
        .ok_or_else(|| PyRuntimeError::new_err("Issue with getting Arial font"))?;
    Ok(arial)
}

#[pyclass(from_py_object)]
#[derive(Clone)]
enum Gradient {
    LinearGradient(f32, f32, f32, f32),
    RadialGradient(f32, f32, f32),
}

#[pyclass(module = "wyvern")]
struct WyvernImage {
    image: Image,
    width: i32,
    height: i32,
    opaque: bool,
}

fn image_info_for(width: i32, height: i32, opaque: bool) -> ImageInfo {
    let alpha = if opaque {
        skia_safe::AlphaType::Opaque
    } else {
        skia_safe::AlphaType::Premul
    };
    ImageInfo::new(
        (width, height),
        ColorType::BGRA8888,
        alpha,
        ColorSpace::new_srgb(),
    )
}

#[pymethods]
impl WyvernImage {
    #[new]
    fn create(
        data: Bound<'_, PyByteArray>,
        width: i32,
        height: i32,
        row_bytes: usize,
    ) -> PyResult<Self> {
        let bytes = unsafe { data.as_bytes() };
        let opaque = bytes.iter().skip(3).step_by(4).all(|&a| a == 255);
        let image_info = image_info_for(width, height, opaque);
        let image = skia_safe::images::raster_from_data(
            &image_info,
            skia_safe::Data::new_copy(bytes),
            row_bytes,
        )
        .ok_or(PyRuntimeError::new_err(
            "Issue with creating image from data",
        ))?;
        Ok(WyvernImage {
            image,
            width,
            height,
            opaque,
        })
    }

    fn scaled(&self, width: i32, height: i32) -> PyResult<WyvernImage> {
        let width = width.max(1);
        let height = height.max(1);
        let image_info = image_info_for(width, height, self.opaque);
        let mut surface = surfaces::raster(&image_info, None, None)
            .ok_or_else(|| PyRuntimeError::new_err("Failed to create scaling surface"))?;
        let dst = Rect::from_wh(width as f32, height as f32);
        surface.canvas().draw_image_rect_with_sampling_options(
            &self.image,
            None,
            dst,
            skia_safe::SamplingOptions::new(
                skia_safe::FilterMode::Linear,
                skia_safe::MipmapMode::None,
            ),
            &Paint::default(),
        );
        let image = surface.image_snapshot();
        Ok(WyvernImage {
            image,
            width,
            height,
            opaque: self.opaque,
        })
    }

    #[getter]
    fn width(&self) -> i32 {
        self.width
    }

    #[getter]
    fn height(&self) -> i32 {
        self.height
    }
}

type CanvasSettings = (Font, Vec<Color4f>, Vec<f32>, Paint);

#[pyclass(unsendable, module = "wyvern")]
struct Canvas {
    skia_surface: skia_safe::Surface,
    path: Option<skia_safe::PathBuilder>,
    font_mgr: FontMgr,
    font: Font,
    gradient_colors: Vec<Color4f>,
    gradient_offsets: Vec<f32>,
    paint: Paint,
    state_stack: Vec<CanvasSettings>,
}

#[pymethods]
impl Canvas {
    fn save(&mut self) {
        self.skia_surface.canvas().save();
        self.state_stack.push((
            self.font.clone(),
            self.gradient_colors.clone(),
            self.gradient_offsets.clone(),
            self.paint.clone(),
        ));
    }

    fn restore(&mut self) -> PyResult<()> {
        self.skia_surface.canvas().restore();
        let (prev_font, prev_gcolor, prev_goff, prev_paint) = self
            .state_stack
            .pop()
            .ok_or(PyRuntimeError::new_err("Restore must be preceded by save"))?;
        self.font = prev_font;
        self.gradient_colors = prev_gcolor;
        self.gradient_offsets = prev_goff;
        self.paint = prev_paint;
        Ok(())
    }

    fn translate(&mut self, x: f32, y: f32) {
        self.skia_surface.canvas().translate(Vector::new(x, y));
    }

    fn rotate(&mut self, angle: f32) {
        self.skia_surface.canvas().rotate(angle * RAD_TO_DEG, None);
    }

    #[pyo3(signature = (xx = 1.0, yx = 0.0, xy = 0.0, yy = 1.0, x0 = 0.0, y0 = 0.0))]
    fn transform(&mut self, xx: f32, yx: f32, xy: f32, yy: f32, x0: f32, y0: f32) {
        let matrix = Matrix::new_all(xx, xy, x0, yx, yy, y0, 0.0, 0.0, 1.0);
        self.skia_surface.canvas().concat(&matrix);
    }

    fn new_path(&mut self) {
        self.path = Some(PathBuilder::new());
    }

    fn move_to(&mut self, x: f32, y: f32) {
        let point = Point::new(x, y);
        self.path
            .get_or_insert_with(|| new_path_and_move(point))
            .move_to(point);
    }

    fn line_to(&mut self, x: f32, y: f32) {
        let point = Point::new(x, y);
        self.path
            .get_or_insert_with(|| new_path_and_move(point))
            .line_to(point);
    }

    fn rel_line_to(&mut self, x: f32, y: f32) -> PyResult<()> {
        self.path
            .as_mut()
            .ok_or_else(|| PyRuntimeError::new_err("Path does not exist for rel_line_to"))?
            .r_line_to(Vector::new(x, y));
        Ok(())
    }

    fn curve_to(&mut self, x1: f32, y1: f32, x2: f32, y2: f32, x3: f32, y3: f32) {
        let first_point = Point::new(x1, y1);
        self.path
            .get_or_insert_with(|| new_path_and_move(first_point))
            .cubic_to(first_point, Point::new(x2, y2), Point::new(x3, y3));
    }

    fn rel_curve_to(
        &mut self,
        x1: f32,
        y1: f32,
        x2: f32,
        y2: f32,
        x3: f32,
        y3: f32,
    ) -> PyResult<()> {
        self.path
            .as_mut()
            .ok_or_else(|| PyRuntimeError::new_err("Path does not exist for rel_curve_to"))?
            .r_cubic_to(
                Vector::new(x1, y1),
                Vector::new(x2, y2),
                Vector::new(x3, y3),
            );
        Ok(())
    }

    fn rectangle(&mut self, left: f32, top: f32, width: f32, height: f32) {
        let r = Rect::new(left, top, left + width, top + height);
        self.path
            .get_or_insert_with(|| new_path_and_move(r.tl()))
            .add_rect(r, None, None);
    }

    fn round_rectangle(
        &mut self,
        left: f32,
        top: f32,
        width: f32,
        height: f32,
        x_rad: f32,
        y_rad: f32,
    ) {
        let r = Rect::new(left, top, left + width, top + height);
        self.path
            .get_or_insert_with(|| new_path_and_move(r.tl()))
            .add_rrect(RRect::new_rect_xy(r, x_rad, y_rad), None, None);
    }

    fn arc(&mut self, xc: f32, yc: f32, radius: f32, angle1: f32, mut angle2: f32) {
        let r = Rect::new(xc - radius, yc - radius, xc + radius, yc + radius);
        let start_point = Point::new(xc + (radius * angle1.cos()), yc + (radius * angle1.sin()));
        while angle2 < angle1 {
            angle2 += 2.0 * PI
        }
        self.path
            .get_or_insert_with(|| new_path_and_line(start_point))
            .add_arc(r, angle1 * RAD_TO_DEG, (angle2 - angle1) * RAD_TO_DEG);
    }

    fn close_path(&mut self) {
        if let Some(pb) = self.path.as_mut() {
            pb.close();
        }
    }

    #[pyo3(signature = (r, g, b, a = None))]
    fn set_source_rgba(&mut self, r: f32, g: f32, b: f32, a: Option<f32>) {
        self.paint.set_shader(None);
        self.paint
            .set_color4f(Color4f::new(r, g, b, a.unwrap_or(1.0)), None);
    }

    fn set_source_rgb(&mut self, r: f32, g: f32, b: f32) {
        self.set_source_rgba(r, g, b, Some(1.0));
    }

    fn set_line_width(&mut self, width: f32) {
        self.paint.set_stroke_width(width);
    }

    fn set_line_join(&mut self, join: LineJoin) {
        match join {
            LineJoin::MITER => self.paint.set_stroke_join(PaintJoin::Miter),
            LineJoin::ROUND => self.paint.set_stroke_join(PaintJoin::Round),
            LineJoin::BEVEL => self.paint.set_stroke_join(PaintJoin::Bevel),
        };
    }

    #[pyo3(signature = (dashes, offset = 0.0))]
    fn set_dash(&mut self, dashes: Vec<f32>, offset: f32) {
        let path_effect = PathEffect::dash(&dashes, offset);
        self.paint.set_path_effect(path_effect);
    }

    fn select_font_face(
        &mut self,
        family_name: String,
        weight: FontWeight,
        slant: FontSlant,
    ) -> PyResult<()> {
        let style = FontStyle::new(
            py_to_skia_weight(weight),
            font_style::Width::NORMAL,
            py_to_skia_slant(slant),
        );
        // legacy_make_typeface falls back to the platform's default face for an
        // unknown family, which is what cairo's select_font_face did (Helvetica on
        // macOS). Falling back to Arial ourselves would render unavailable fonts
        // differently than cairo did.
        if let Some(typeface) = self
            .font_mgr
            .legacy_make_typeface(Some(family_name.as_str()), style)
        {
            self.font.set_typeface(typeface);
        } else {
            self.font.set_typeface(get_arial(&self.font_mgr, style)?);
        }
        Ok(())
    }

    fn set_font_size(&mut self, size: f32) -> PyResult<()> {
        self.font.set_size(size);
        Ok(())
    }

    fn text_extents(&mut self, text: String) -> PyResult<(f32, f32, f32, f32, f32, f32)> {
        let font = self.font.as_ref();
        let (width, _) = Font::measure_str(font, &text, Some(&self.paint));
        // Font::measure_str's bounds are the rasterizer's glyph-mask bounds, which
        // are rounded out to whole pixels and padded for anti-aliasing. Cairo's
        // text_extents reports the exact outline ink extents, so measure the text
        // path instead to keep label dimensions the same as they were under cairo.
        let rect = Path::from_str(&text, ORIGIN, font).compute_tight_bounds();
        Ok((
            rect.left(),
            rect.top(),
            rect.right() - rect.left(),
            rect.height(),
            width,
            rect.bottom(),
        ))
    }

    fn text_path(&mut self, text: String) -> PyResult<()> {
        let font = self.font.as_ref();
        let point = self
            .path
            .as_ref()
            .and_then(|pb| pb.get_last_pt())
            .unwrap_or(ORIGIN);
        let text_path = Path::from_str(&text, point, font);
        self.path
            .get_or_insert(PathBuilder::new_path(&text_path))
            .add_path(&text_path, None);
        Ok(())
    }

    fn show_text(&mut self, text: String) -> PyResult<()> {
        let font = self.font.as_ref();
        let point = self
            .path
            .as_ref()
            .and_then(|pb| pb.get_last_pt())
            .unwrap_or(ORIGIN);
        let mut paint = self.paint.clone();
        paint.set_stroke(false);
        paint.set_anti_alias(true);
        self.skia_surface
            .canvas()
            .draw_str(&text, point, font, &paint);
        Ok(())
    }

    fn paint_with_alpha(&mut self, a: f32) {
        let mut paint = self.paint.clone();
        paint.set_alpha_f(a);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_paint(&paint);
    }

    fn clip_preserve(&mut self) -> PyResult<()> {
        let path = if let Some(pb) = &self.path {
            Ok(pb.snapshot())
        } else {
            Err(PyRuntimeError::new_err(
                "Path does not exist for clip_preserve",
            ))
        }?;
        self.skia_surface.canvas().clip_path(&path, None, true);
        Ok(())
    }

    fn clip(&mut self) -> PyResult<()> {
        let path = self
            .path
            .take()
            .ok_or(PyRuntimeError::new_err("Path does not exist for clip"))?
            .detach();
        self.skia_surface.canvas().clip_path(&path, None, true);
        Ok(())
    }

    fn stroke_preserve(&mut self) -> PyResult<()> {
        let path = if let Some(pb) = &self.path {
            Ok(pb.snapshot())
        } else {
            Err(PyRuntimeError::new_err(
                "Path does not exist for stroke_preserve",
            ))
        }?;
        let mut paint = self.paint.clone();
        paint.set_stroke(true);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }

    fn stroke(&mut self) -> PyResult<()> {
        let path = self
            .path
            .take()
            .ok_or(PyRuntimeError::new_err("Path does not exist for stroke"))?
            .detach();
        let mut paint = self.paint.clone();
        paint.set_stroke(true);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }

    fn fill_preserve(&mut self) -> PyResult<()> {
        let path = if let Some(pb) = &self.path {
            Ok(pb.snapshot())
        } else {
            Err(PyRuntimeError::new_err(
                "Path does not exist for fill_preserve",
            ))
        }?;
        let mut paint = self.paint.clone();
        paint.set_stroke(false);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }

    fn fill(&mut self) -> PyResult<()> {
        let path = self
            .path
            .take()
            .ok_or(PyRuntimeError::new_err("Path does not exist for fill"))?
            .detach();
        let mut paint = self.paint.clone();
        paint.set_stroke(false);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }

    fn add_color_stop_rgba(&mut self, offset: f32, r: f32, g: f32, b: f32, a: f32) {
        self.gradient_offsets.push(offset);
        self.gradient_colors.push(Color4f::new(r, g, b, a));
    }

    fn set_source_linear_gradient(&mut self, x0: f32, y0: f32, x1: f32, y1: f32) -> PyResult<()> {
        let gradient = gradient::Gradient::new(
            gradient::Colors::new(
                &self.gradient_colors,
                Some(&self.gradient_offsets),
                TileMode::Clamp,
                None,
            ),
            gradient::Interpolation::default(),
        );
        let shader = gradient::shaders::linear_gradient(
            (Point::new(x0, y0), Point::new(x1, y1)),
            &gradient,
            None,
        )
        .ok_or(PyRuntimeError::new_err(
            "Issue with creating linear gradient shader (did you add color stops?)",
        ))?;
        self.paint.set_shader(shader);
        Ok(())
    }

    fn set_source_radial_gradient(&mut self, xc: f32, yc: f32, radius: f32) -> PyResult<()> {
        let gradient = gradient::Gradient::new(
            gradient::Colors::new(
                &self.gradient_colors,
                Some(&self.gradient_offsets),
                TileMode::Clamp,
                None,
            ),
            gradient::Interpolation::default(),
        );
        let shader =
            gradient::shaders::radial_gradient((Point::new(xc, yc), radius), &gradient, None)
                .ok_or(PyRuntimeError::new_err(
                    "Issue with creating radial gradient shader (did you add color stops?)",
                ))?;
        self.paint.set_shader(shader);
        Ok(())
    }

    fn set_source_gradient(&mut self, g: Gradient) -> PyResult<()> {
        match g {
            Gradient::LinearGradient(x0, y0, x1, y1) => {
                self.set_source_linear_gradient(x0, y0, x1, y1)?
            }
            Gradient::RadialGradient(xc, yc, radius) => {
                self.set_source_radial_gradient(xc, yc, radius)?
            }
        }
        self.gradient_offsets.clear();
        self.gradient_colors.clear();
        Ok(())
    }

    fn draw_image(&mut self, image: &WyvernImage, x: f32, y: f32, a: f32) {
        let mut paint = Paint::default();
        paint.set_alpha_f(a);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_image_with_sampling_options(
            &image.image,
            Point::new(x, y),
            skia_safe::SamplingOptions::new(
                skia_safe::FilterMode::Linear,
                skia_safe::MipmapMode::None,
            ),
            Some(&paint),
        );
    }

    fn scale_canvas(&mut self, scale_factor: f64) {
        self.skia_surface
            .canvas()
            .scale((scale_factor as f32, scale_factor as f32));
    }
}

#[pyclass(module = "wyvern", subclass)]
struct ImageSurface {
    width: i32,
    height: i32,
    canvas: Py<Canvas>,
}

#[pymethods]
impl ImageSurface {
    #[new]
    #[pyo3(signature = (width, height, scale_factor = 1.0))]
    fn create(width: i32, height: i32, scale_factor: f64) -> PyResult<Self> {
        Python::attach(|py| {
            let skia_surface = create_skia_surface(width, height, scale_factor)?;
            let font_mgr = FontMgr::new();
            let style = FontStyle::new(
                font_style::Weight::NORMAL,
                font_style::Width::NORMAL,
                font_style::Slant::Upright,
            );
            let arial = get_arial(&font_mgr, style)?;
            let canvas = Py::new(
                py,
                Canvas {
                    skia_surface,
                    path: None,
                    font_mgr,
                    font: Font::from_typeface(arial, 12.0),
                    gradient_colors: Vec::new(),
                    gradient_offsets: Vec::new(),
                    paint: Paint::default(),
                    state_stack: Vec::new(),
                },
            )?;
            Ok(ImageSurface {
                width,
                height,
                canvas,
            })
        })
    }

    #[getter]
    fn width(&self) -> i32 {
        self.width
    }

    #[getter]
    fn height(&self) -> i32 {
        self.height
    }

    #[getter]
    fn canvas(&self, py: Python<'_>) -> Py<Canvas> {
        self.canvas.clone_ref(py)
    }

    #[getter]
    fn data(&self, py: Python<'_>) -> PyResult<Py<PyByteArray>> {
        let mut canvas_ref = self.canvas.bind(py).borrow_mut();
        let pixmap = canvas_ref
            .skia_surface
            .peek_pixels()
            .ok_or_else(|| PyRuntimeError::new_err("Could not read pixel data from canvas"))?;
        let bytes = pixmap
            .bytes()
            .ok_or_else(|| PyRuntimeError::new_err("Could not read pixel data from canvas"))?;
        Ok(PyByteArray::new(py, bytes).unbind())
    }

    #[setter]
    fn set_width(&mut self, width: i32) {
        self.width = width;
    }

    #[setter]
    fn set_height(&mut self, height: i32) {
        self.height = height;
    }
}
/* WYVERN */

/* BYEGAME */
use std::num::NonZero;
use std::rc::Rc;
use std::sync::OnceLock;
use std::time::{Duration, Instant};
use winit::application::ApplicationHandler;
use winit::dpi::{PhysicalPosition, PhysicalSize};
use winit::event::{Modifiers, WindowEvent};
use winit::event_loop::{ActiveEventLoop, ControlFlow, EventLoop, EventLoopProxy};
use winit::keyboard::{Key, NamedKey};
use winit::window::{Window, WindowAttributes, WindowId};

enum UserEvent {
    Quit,
}

// apparently this is idiomatic
static PROXY: OnceLock<EventLoopProxy<UserEvent>> = OnceLock::new();

struct AppInternals {
    window: Rc<Window>,
    softbuffer_surface: softbuffer::Surface<Rc<Window>, Rc<Window>>,
}

struct WinitApp {
    window_attributes: WindowAttributes,
    internals: Option<AppInternals>,
    last_tick: Instant,
    last_mouse: Instant,
    cursor_position: PhysicalPosition<f64>,
    py_surface: Option<Py<ImageSurface>>,
    on_event: Py<PyAny>,
    modifiers: Modifiers,
    error: Option<PyErr>,
}

#[pyclass(from_py_object)]
#[derive(Clone)]
pub struct MouseEvent {
    #[pyo3(get)]
    pub x: f64,
    #[pyo3(get)]
    pub y: f64,
    #[pyo3(get)]
    pub button: u8,
}

fn winit_button_to_int(button: winit::event::MouseButton) -> u8 {
    match button {
        winit::event::MouseButton::Left => 0,
        winit::event::MouseButton::Middle => 1,
        winit::event::MouseButton::Right => 2,
        _ => 0,
    }
}

#[pyclass(from_py_object)]
#[derive(Clone)]
pub struct KeyEvent {
    #[pyo3(get)]
    pub key: String,
    #[pyo3(get)]
    pub is_named: bool,
    #[pyo3(get)]
    pub modifiers: Vec<String>,
}

fn named_keys_to_name(name: &NamedKey) -> Option<&str> {
    match name {
        NamedKey::ArrowLeft => Some("left"),
        NamedKey::ArrowRight => Some("right"),
        NamedKey::ArrowDown => Some("down"),
        NamedKey::ArrowUp => Some("up"),

        NamedKey::Enter => Some("enter"),
        NamedKey::Tab => Some("tab"),
        NamedKey::Escape => Some("escape"),
        NamedKey::Backspace => Some("backspace"),
        NamedKey::Delete => Some("delete"),
        NamedKey::Space => Some("space"),
        _ => None
    }
}

fn modifiers_to_vec(modifiers: &winit::event::Modifiers) -> Vec<String> {
    let mut result = Vec::new();
    let state = modifiers.state();
    if state.shift_key() {
        result.push("shift".to_string());
    }
    if state.control_key() {
        result.push("control".to_string());
    }
    if state.alt_key() {
        result.push("meta".to_string());
    }
    result
}

#[pyclass(from_py_object)]
#[derive(Clone)]
pub struct ResizeEvent {
    #[pyo3(get)]
    pub width: u32,
    #[pyo3(get)]
    pub height: u32,
}

#[pyclass(from_py_object)]
#[derive(Clone)]
pub struct InitEvent {
    #[pyo3(get, set)]
    pub width: u32,
    #[pyo3(get, set)]
    pub height: u32,
    #[pyo3(get, set)]
    pub resizable: bool,
    #[pyo3(get, set)]
    pub title: String,
}

#[pymethods]
impl InitEvent {
    #[new]
    fn create(width: u32, height: u32, resizable: bool, title: String) -> Self {
        InitEvent {
            width,
            height,
            resizable,
            title,
        }
    }
}

#[pyclass(from_py_object)]
#[derive(Clone)]
pub struct PythonEvent {
    #[pyo3(get)]
    pub event_type: String,
    #[pyo3(get)]
    pub mouse: Option<MouseEvent>,
    #[pyo3(get)]
    pub key: Option<KeyEvent>,
    #[pyo3(get)]
    pub resize: Option<ResizeEvent>,
}

impl PythonEvent {
    pub fn mouse_press(x: f64, y: f64, button: u8) -> Self {
        PythonEvent {
            event_type: "mouse_press".to_string(),
            mouse: Some(MouseEvent { x, y, button }),
            key: None,
            resize: None,
        }
    }

    pub fn mouse_release(x: f64, y: f64, button: u8) -> Self {
        PythonEvent {
            event_type: "mouse_release".to_string(),
            mouse: Some(MouseEvent { x, y, button }),
            key: None,
            resize: None,
        }
    }

    pub fn mouse_move(x: f64, y: f64) -> Self {
        PythonEvent {
            event_type: "mouse_move".to_string(),
            mouse: Some(MouseEvent { x, y, button: 0 }),
            key: None,
            resize: None,
        }
    }

    pub fn mouse_drag(x: f64, y: f64, button: u8) -> Self {
        PythonEvent {
            event_type: "mouse_drag".to_string(),
            mouse: Some(MouseEvent { x, y, button }),
            key: None,
            resize: None,
        }
    }

    pub fn key_press(key: String, is_named: bool, modifiers: Vec<String>) -> Self {
        PythonEvent {
            event_type: "key_press".to_string(),
            mouse: None,
            key: Some(KeyEvent {
                key,
                is_named,
                modifiers,
            }),
            resize: None,
        }
    }

    pub fn key_release(key: String, is_named: bool, modifiers: Vec<String>) -> Self {
        PythonEvent {
            event_type: "key_release".to_string(),
            mouse: None,
            key: Some(KeyEvent {
                key,
                is_named,
                modifiers,
            }),
            resize: None,
        }
    }

    pub fn resize(width: u32, height: u32) -> Self {
        PythonEvent {
            event_type: "resize".to_string(),
            mouse: None,
            key: None,
            resize: Some(ResizeEvent { width, height }),
        }
    }

    pub fn init() -> Self {
        PythonEvent {
            event_type: "init".to_string(),
            mouse: None,
            key: None,
            resize: None,
        }
    }

    pub fn quit() -> Self {
        PythonEvent {
            event_type: "quit".to_string(),
            mouse: None,
            key: None,
            resize: None,
        }
    }

    pub fn step() -> Self {
        PythonEvent {
            event_type: "step".to_string(),
            mouse: None,
            key: None,
            resize: None,
        }
    }

    pub fn redraw() -> Self {
        PythonEvent {
            event_type: "redraw".to_string(),
            mouse: None,
            key: None,
            resize: None,
        }
    }
}

impl WinitApp {
    fn call_event_handler(
        &mut self,
        event_loop: &ActiveEventLoop,
        event: PythonEvent,
    ) -> Option<InitEvent> {
        let mut request_redraw = true;
        let handler_result = Python::attach(|py| -> PyResult<Option<InitEvent>> {
            if event.event_type == "init" {
                let attributes = self.on_event.call1(py, (event,))?.extract(py)?;
                request_redraw = false;
                Ok(Some(attributes))
            } else {
                let Some(py_surface) = self.py_surface.as_ref() else {
                    self.error = Some(PyRuntimeError::new_err(
                        "Surface does not exist for event handler",
                    ));
                    event_loop.exit();
                    return Ok(None);
                };
                self.on_event.call1(py, (event, py_surface.clone_ref(py)))?;
                Ok(None)
            }
        });

        let res = match handler_result {
            Ok(res) => res,
            Err(err) => {
                self.error = Some(err);
                event_loop.exit();
                return None;
            }
        };
        if request_redraw {
            if let Some(internals) = self.internals.as_ref() {
                internals.window.request_redraw()
            } else {
                println!("why are we here");
                self.error = Some(PyRuntimeError::new_err("Issue with redrawing window"));
                event_loop.exit();
            }
        }
        res
    }
}

impl ApplicationHandler<UserEvent> for WinitApp {
    fn resumed(&mut self, event_loop: &ActiveEventLoop) {
        if self.internals.is_none() {
            let Some(attribs) = self.call_event_handler(event_loop, PythonEvent::init()) else {
                self.error = Some(PyRuntimeError::new_err("Issue with init event"));
                return
            };
            let Ok(image) = image::open("scotty.png") else {
                self.error = Some(PyRuntimeError::new_err("Issue with opening icon image"));
                return
            };
            let image_rgba = image.into_rgba8();
            let (width, height) = image_rgba.dimensions();
            let rgba = image_rgba.into_raw();
            let Ok(icon) = winit::window::Icon::from_rgba(rgba, width, height) else {
                self.error = Some(PyRuntimeError::new_err("Issue with creating icon image"));
                return
            };
            self.window_attributes = std::mem::take(&mut self.window_attributes)
                .with_inner_size(PhysicalSize::new(attribs.width, attribs.height))
                .with_resizable(attribs.resizable)
                .with_title(attribs.title)
                .with_window_icon(Some(icon))
                .with_visible(false);
        }

        let window = if let Ok(window) = event_loop.create_window(self.window_attributes.clone()) {
            // make the window centered
            if let Some(monitor) = window.current_monitor() {
                let screen_size = monitor.size();
                let window_size = window.outer_size();

                let x = (screen_size.width.saturating_sub(window_size.width) / 2) as i32
                    + monitor.position().x;
                let y = (screen_size.height.saturating_sub(window_size.height) / 2) as i32
                    + monitor.position().y;

                window.set_outer_position(PhysicalPosition::new(x, y));
            }
            Rc::new(window)
        } else {
            self.error = Some(PyRuntimeError::new_err("Issue with creating window"));
            return;
        };
        let softbuffer_surface = {
            let Ok(context) = softbuffer::Context::new(window.clone()) else {
                self.error = Some(PyRuntimeError::new_err(
                    "Issue with creating context for softbuffer surface",
                ));
                return;
            };
            let Ok(surface) = softbuffer::Surface::new(&context, window.clone()) else {
                self.error = Some(PyRuntimeError::new_err(
                    "Issue with creating softbuffer surface",
                ));
                return;
            };
            surface
        };

        let scale_factor = window.scale_factor();
        let (phys_width, phys_height) = {
            let size = window.inner_size();
            (size.width, size.height)
        };
        let py_surface = ImageSurface::create(phys_width as i32, phys_height as i32, scale_factor);

        if let Err(err) = Python::attach(|py| -> PyResult<()> {
            let py_surface = Py::new(py, py_surface?)?;
            self.py_surface = Some(py_surface);
            Ok(())
        }) {
            self.error = Some(err);
            event_loop.exit();
        };

        window.set_visible(true);

        self.internals = Some(AppInternals {
            window,
            softbuffer_surface,
        });

        self.call_event_handler(event_loop, PythonEvent::redraw());
    }

    fn about_to_wait(&mut self, event_loop: &ActiveEventLoop) {
        let fps = 30;
        let elapsed = self.last_tick.elapsed();
        if elapsed >= Duration::from_millis(1000 / fps) {
            self.call_event_handler(event_loop, PythonEvent::step());
            self.last_tick = Instant::now();
        }
    }

    fn window_event(&mut self, event_loop: &ActiveEventLoop, _id: WindowId, event: WindowEvent) {
        let Some(app_internals) = self.internals.as_mut() else {
            return;
        };
        let Some(py_surface) = self.py_surface.as_mut() else {
            return;
        };

        let AppInternals {
            window,
            softbuffer_surface,
        } = app_internals;

        match event {
            WindowEvent::CloseRequested => {
                event_loop.exit();
            }
            WindowEvent::Resized(new_size) => {
                let Some(new_width) = NonZero::new(new_size.width) else {
                    self.error = Some(PyRuntimeError::new_err("New window width must be non-zero"));
                    event_loop.exit();
                    return;
                };
                let Some(new_height) = NonZero::new(new_size.height) else {
                    self.error = Some(PyRuntimeError::new_err(
                        "New window height must be non-zero",
                    ));
                    event_loop.exit();
                    return;
                };

                if softbuffer_surface.resize(new_width, new_height).is_err() {
                    self.error = Some(PyRuntimeError::new_err(
                        "Issue with resizing softbuffer surface",
                    ));
                    event_loop.exit()
                };

                Python::attach(|py| {
                    let mut surface_ref = py_surface.borrow_mut(py);
                    let mut canvas = surface_ref.canvas.bind(py).borrow_mut();
                    canvas.scale_canvas(window.scale_factor());
                    surface_ref.width = new_size.width as i32;
                    surface_ref.height = new_size.height as i32;
                });

                // self.call_event_handler(
                //     event_loop,
                //     PythonEvent::resize(new_size.width, new_size.height),
                // );
            }
            WindowEvent::CursorMoved {
                device_id: _,
                position,
            } => {
                if self.last_mouse.elapsed() < Duration::from_millis(1000 / 30) {
                    return;
                }
                self.cursor_position = position;
                let scale = window.scale_factor();
                self.call_event_handler(
                    event_loop,
                    PythonEvent::mouse_move(position.x / scale, position.y / scale),
                );
                self.last_mouse = Instant::now();
            }
            WindowEvent::MouseInput {
                device_id: _,
                state,
                button,
            } => {
                let scale = window.scale_factor();
                match state {
                    winit::event::ElementState::Pressed => {
                        self.call_event_handler(
                            event_loop,
                            PythonEvent::mouse_press(
                                self.cursor_position.x / scale,
                                self.cursor_position.y / scale,
                                winit_button_to_int(button),
                            ),
                        );
                    }
                    winit::event::ElementState::Released => {
                        self.call_event_handler(
                            event_loop,
                            PythonEvent::mouse_release(
                                self.cursor_position.x / scale,
                                self.cursor_position.y / scale,
                                winit_button_to_int(button),
                            ),
                        );
                    }
                }
            }
            WindowEvent::RedrawRequested => {
                let Ok(mut buffer) = softbuffer_surface.buffer_mut() else {
                    self.error = Some(PyRuntimeError::new_err(
                        "Issue with obtaining softbuffer surface",
                    ));
                    event_loop.exit();
                    return;
                };
                Python::attach(|py| {
                    if let Ok(bytearray) = py_surface.borrow_mut(py).data(py) {
                        let bytes = unsafe { bytearray.bind(py).as_bytes() };
                        let safe_len = buffer.len().min(bytes.len() / 4);
                        for (i, pixel) in buffer.iter_mut().take(safe_len).enumerate() {
                            let offset = i * 4;
                            let r = bytes[offset] as u32;
                            let g = bytes[offset + 1] as u32;
                            let b = bytes[offset + 2] as u32;
                            *pixel = (r << 16) | (g << 8) | b;
                        }
                        if safe_len < buffer.len() {
                            return;
                        }
                        if buffer.present().is_err() {
                            self.error =
                                Some(PyRuntimeError::new_err("Issue presenting to buffer"));
                            event_loop.exit()
                        }
                    } else {
                        self.error = Some(PyRuntimeError::new_err("Issue getting canvas data"));
                        event_loop.exit()
                    }
                });

                self.call_event_handler(event_loop, PythonEvent::redraw());
            }
            WindowEvent::KeyboardInput {
                device_id: _,
                event,
                is_synthetic,
            } => {
                if is_synthetic {
                    return;
                }
                let mut is_named = false;
                let key = match &event.logical_key {
                    Key::Character(s) => s,
                    Key::Named(name) => {
                        is_named = true;
                        let Some(name) = named_keys_to_name(name) else {
                            return;
                        };
                        name
                    }
                    _ => return,
                };
                match event.state {
                    winit::event::ElementState::Pressed => {
                        self.call_event_handler(
                            event_loop,
                            PythonEvent::key_press(
                                key.to_string(),
                                is_named,
                                modifiers_to_vec(&self.modifiers),
                            ),
                        );
                    }
                    winit::event::ElementState::Released => {
                        self.call_event_handler(
                            event_loop,
                            PythonEvent::key_release(
                                key.to_string(),
                                is_named,
                                modifiers_to_vec(&self.modifiers),
                            ),
                        );
                    }
                }
            }
            WindowEvent::ModifiersChanged(new_modifiers) => {
                self.modifiers = new_modifiers;
            }
            _ => (),
        }
    }

    fn user_event(&mut self, event_loop: &ActiveEventLoop, event: UserEvent) {
        match event {
            UserEvent::Quit => {
                self.call_event_handler(event_loop, PythonEvent::quit());
                event_loop.exit()
            }
        }
    }
}

#[pyfunction]
fn run(on_event: Py<PyAny>) -> PyResult<()> {
    let mut app = WinitApp {
        window_attributes: Window::default_attributes(),
        internals: None,
        last_tick: Instant::now(),
        last_mouse: Instant::now(),
        cursor_position: PhysicalPosition { x: 0.0, y: 0.0 },
        py_surface: None,
        on_event,
        modifiers: Modifiers::default(),
        error: None,
    };

    let event_loop = EventLoop::<UserEvent>::with_user_event()
        .build()
        .map_err(|_| PyRuntimeError::new_err("Issue with starting event loop"))?;
    event_loop.set_control_flow(ControlFlow::Poll);
    PROXY
        .set(event_loop.create_proxy())
        .map_err(|_| PyRuntimeError::new_err("Issue with starting proxy event loop"))?;
    let _ = event_loop.run_app(&mut app);

    match app.error {
        None => Ok(()),
        Some(err) => Err(err),
    }
}

#[pyfunction]
fn quit() -> PyResult<()> {
    let proxy = PROXY
        .get()
        .ok_or_else(|| PyRuntimeError::new_err("Event loop proxy is not running"))?;
    proxy
        .send_event(UserEvent::Quit)
        .map_err(|_| PyRuntimeError::new_err("Failed to send quit event"))?;
    Ok(())
}
/* BYEGAME */

#[pymodule]
fn cmu_graphics_helpers(m: &Bound<'_, PyModule>) -> PyResult<()> {
    let pygeo = PyModule::new(m.py(), "pygeo")?;
    pygeo.add_function(wrap_pyfunction!(union, &pygeo)?)?;
    m.add_submodule(&pygeo)?;
    m.py()
        .import("sys")?
        .getattr("modules")?
        .set_item("cmu_graphics_helpers.pygeo", pygeo)?;

    let wyvern = PyModule::new(m.py(), "wyvern")?;
    wyvern.add_class::<ImageSurface>()?;
    wyvern.add_class::<Canvas>()?;
    wyvern.add_class::<LineJoin>()?;
    wyvern.add_class::<FontWeight>()?;
    wyvern.add_class::<FontSlant>()?;
    wyvern.add_class::<Gradient>()?;
    wyvern.add_class::<WyvernImage>()?;
    wyvern.add_class::<PythonEvent>()?;
    wyvern.add_class::<MouseEvent>()?;
    wyvern.add_class::<KeyEvent>()?;
    wyvern.add_class::<ResizeEvent>()?;
    wyvern.add_class::<InitEvent>()?;
    wyvern.add_function(wrap_pyfunction!(run, &wyvern)?)?;
    wyvern.add_function(wrap_pyfunction!(quit, &wyvern)?)?;
    m.add_submodule(&wyvern)?;
    m.py()
        .import("sys")?
        .getattr("modules")?
        .set_item("cmu_graphics_helpers.wyvern", wyvern)?;
    Ok(())
}
