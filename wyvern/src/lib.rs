use std::f32::consts::*;

use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
use pyo3::types::PyByteArray;

use skia_safe::{
    font_style, gradient, surfaces, Color, Color4f, ColorSpace, ColorType, Font, FontMgr,
    FontStyle, ImageInfo, Matrix, Paint, PaintJoin, Path, PathBuilder, PathEffect, Point, RRect,
    Rect, Vector,
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

fn new_path_and_move(p: Point) -> PathBuilder {
    let mut new_path = PathBuilder::new();
    new_path.move_to(p);
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

#[pyclass(from_py_object)]
#[derive(Clone)]
enum Gradient {
    LinearGradient(f32, f32, f32, f32),
    RadialGradient(f32, f32, f32),
}

type CanvasSettings = (
    Option<PathBuilder>,
    Option<Font>,
    Vec<Color4f>,
    Vec<f32>,
    Paint,
);

#[pyclass(unsendable, module = "wyvern")]
struct Canvas {
    skia_surface: skia_safe::Surface,
    path: Option<skia_safe::PathBuilder>,
    font: Option<skia_safe::Font>,
    gradient_colors: Vec<Color4f>,
    gradient_offsets: Vec<f32>,
    paint: Paint,
    state_stack: Vec<CanvasSettings>,
}

impl Canvas {
    fn save(&mut self) {
        self.skia_surface.canvas().save();
        self.state_stack.push((
            self.path.clone(),
            self.font.clone(),
            self.gradient_colors.clone(),
            self.gradient_offsets.clone(),
            self.paint.clone(),
        ));
    }

    fn restore(&mut self) {
        self.skia_surface.canvas().restore();
        let (prev_path, prev_font, prev_gcolor, prev_goff, prev_paint) = self
            .state_stack
            .pop()
            .unwrap_or((None, None, Vec::new(), Vec::new(), Paint::default()));
        self.path = prev_path;
        self.font = prev_font;
        self.gradient_colors = prev_gcolor;
        self.gradient_offsets = prev_goff;
        self.paint = prev_paint;
    }

    fn translate(&mut self, x: f32, y: f32) {
        self.skia_surface.canvas().translate(Vector::new(x, y));
    }

    fn rotate(&mut self, angle: f32) {
        self.skia_surface
            .canvas()
            .rotate(angle * (180.0 / PI), None);
    }

    fn transform(
        &mut self,
        scale_x: f32,
        skew_y: f32,
        skew_x: f32,
        scale_y: f32,
        trans_x: f32,
        trans_y: f32,
    ) {
        let matrix = Matrix::new_all(
            scale_x, skew_x, trans_x, skew_y, scale_y, trans_y, 0.0, 0.0, 1.0,
        );
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

    fn round_rectangle(&mut self, left: f32, top: f32, width: f32, height: f32) {
        let r = Rect::new(left, top, left + width, top + height);
        self.path
            .get_or_insert_with(|| new_path_and_move(r.tl()))
            .add_rrect(RRect::new_rect(r), None, None);
    }

    fn arc(&mut self, xc: f32, yc: f32, radius: f32, angle1: f32, mut angle2: f32) {
        let r = Rect::new(xc - radius, yc - radius, xc + radius, yc + radius);
        let start_point = Point::new(xc + (radius * angle1.cos()), yc + (radius * angle1.sin()));
        while angle2 < angle1 {
            angle2 += 2.0 * PI
        }
        self.path
            .get_or_insert_with(|| new_path_and_move(start_point))
            .line_to(start_point)
            .add_arc(r, angle1 * (180.0 / PI), (angle2 - angle1) * (180.0 / PI));
    }

    fn close_path(&mut self) {
        if let Some(pb) = self.path.as_mut() {
            pb.close();
        }
    }

    fn set_source_rgba(&mut self, r: f32, g: f32, b: f32, a: Option<f32>) {
        let color_space = self.skia_surface.image_info().color_space();
        self.paint
            .set_color4f(Color4f::new(r, g, b, a.unwrap_or(1.0)), &color_space);
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

    fn set_dash(&mut self, intervals: Vec<f32>, phase: f32) {
        let path_effect = PathEffect::dash(&intervals, phase);
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
        let typeface = FontMgr::new()
            .match_family_style(&family_name, style)
            .ok_or_else(|| PyRuntimeError::new_err("Font family could not be found"))?;
        let size = self.font.as_ref().map(|f| f.size()).unwrap_or(12.0);
        self.font = Some(Font::from_typeface(typeface, size));
        Ok(())
    }

    fn set_font_size(&mut self, size: f32) -> PyResult<()> {
        let font = self
            .font
            .take()
            .ok_or_else(|| PyRuntimeError::new_err("Font face required for set_font_size"))?;
        self.font = Some(Font::from_typeface(font.typeface(), size));
        Ok(())
    }

    fn text_extents(&mut self, text: String) -> PyResult<(f32, f32, f32, f32, f32, f32)> {
        let font = self
            .font
            .as_ref()
            .ok_or_else(|| PyRuntimeError::new_err("Font face required for text_extents"))?;
        let (width, rect) = Font::measure_str(font, text, Some(&self.paint));
        Ok((
            rect.left(),
            rect.top(),
            width,
            rect.height(),
            rect.right(),
            rect.bottom(),
        ))
    }

    fn text_path(&mut self, text: String) -> PyResult<()> {
        let font = self
            .font
            .as_ref()
            .ok_or_else(|| PyRuntimeError::new_err("Font face required for text_path"))?;
        let point = self
            .path
            .as_ref()
            .and_then(|pb| pb.snapshot().last_pt())
            .unwrap_or_else(|| Point::new(0.0, 0.0));
        let text_path = Path::from_str(&text, point, font);
        self.path
            .get_or_insert(PathBuilder::new_path(&text_path))
            .add_path(&text_path);
        Ok(())
    }

    fn show_text(&mut self, text: String) -> PyResult<()> {
        let font = self
            .font
            .as_ref()
            .ok_or_else(|| PyRuntimeError::new_err("Font face required for text_path"))?;
        let point = self
            .path
            .as_ref()
            .and_then(|pb| pb.snapshot().last_pt())
            .unwrap_or_else(|| Point::new(0.0, 0.0));
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
        self.skia_surface.canvas().draw_paint(&paint);
    }

    fn clip_preserve(&mut self) -> PyResult<()> {
        let path = self
            .path
            .clone()
            .ok_or(PyRuntimeError::new_err("Path does not exist for clip"))?
            .detach();
        self.skia_surface.canvas().clip_path(&path, None, true);
        Ok(())
    }

    fn clip(&mut self) -> PyResult<()> {
        self.clip_preserve()?;
        self.path = None;
        Ok(())
    }

    fn stroke_preserve(&mut self) -> PyResult<()> {
        let path = self
            .path
            .clone()
            .ok_or(PyRuntimeError::new_err("Path does not exist for stroke"))?
            .detach();
        let mut paint = self.paint.clone();
        paint.set_stroke(true);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }

    fn stroke(&mut self) -> PyResult<()> {
        self.stroke_preserve()?;
        self.path = None;
        Ok(())
    }

    fn fill_preserve(&mut self) -> PyResult<()> {
        let path = self
            .path
            .clone()
            .ok_or(PyRuntimeError::new_err("Path does not exist for fill"))?
            .detach();
        let mut paint = self.paint.clone();
        paint.set_stroke(false);
        paint.set_anti_alias(true);
        self.skia_surface.canvas().draw_path(&path, &paint);
        Ok(())
    }

    fn fill(&mut self) -> PyResult<()> {
        self.fill_preserve()?;
        self.path = None;
        Ok(())
    }

    fn add_color_stop_rgba(&mut self, offset: f32, color: Color4f) {
        self.gradient_offsets.push(offset);
        self.gradient_colors.push(color);
    }

    fn set_source_linear_gradient(&mut self, x0: f32, y0: f32, x1: f32, y1: f32) -> PyResult<()> {
        let colors = &self.gradient_colors.clone();
        let offsets = &self.gradient_offsets.clone();
        let gradient = gradient::Gradient::new(
            gradient::Colors::new(colors, Some(offsets), skia_safe::TileMode::Clamp, None),
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
        let colors = &self.gradient_colors.clone();
        let offsets = &self.gradient_offsets.clone();
        let gradient = gradient::Gradient::new(
            gradient::Colors::new(colors, Some(offsets), skia_safe::TileMode::Clamp, None),
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
        self.gradient_offsets = Vec::new();
        self.gradient_colors = Vec::new();
        Ok(())
    }

    fn set_source_image(
        &mut self,
        data: &mut [u8],
        width: i32,
        height: i32,
        row_bytes: usize,
        x: f32,
        y: f32,
    ) -> PyResult<()> {
        let image_info = ImageInfo::new(
            (width, height),
            ColorType::BGRA8888,
            skia_safe::AlphaType::Premul,
            ColorSpace::new_srgb(),
        );
        let image = skia_safe::images::raster_from_data(
            &image_info,
            skia_safe::Data::new_copy(data),
            row_bytes,
        )
        .ok_or(PyRuntimeError::new_err(
            "Issue with creating image from data",
        ))?;
        self.skia_surface
            .canvas()
            .draw_image(image, Point::new(x, y), Some(&self.paint));
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
fn translate(ctx: Py<Canvas>, x: f32, y: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().translate(x, y);
    ctx
}

#[pyfunction]
fn rotate(ctx: Py<Canvas>, angle: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().rotate(angle);
    ctx
}

#[pyfunction]
#[pyo3(signature = (ctx, xx = 1.0, yx = 0.0, xy = 0.0, yy = 1.0, x0 = 0.0, y0 = 0.0))]
fn transform(
    ctx: Py<Canvas>,
    xx: f32,
    yx: f32,
    xy: f32,
    yy: f32,
    x0: f32,
    y0: f32,
    py: Python<'_>,
) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().transform(xx, yx, xy, yy, x0, y0);
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
fn curve_to(
    ctx: Py<Canvas>,
    x1: f32,
    y1: f32,
    x2: f32,
    y2: f32,
    x3: f32,
    y3: f32,
    py: Python<'_>,
) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().curve_to(x1, y1, x2, y2, x3, y3);
    ctx
}

#[pyfunction]
fn rel_curve_to(
    ctx: Py<Canvas>,
    x1: f32,
    y1: f32,
    x2: f32,
    y2: f32,
    x3: f32,
    y3: f32,
    py: Python<'_>,
) -> PyResult<Py<Canvas>> {
    ctx.bind(py)
        .borrow_mut()
        .rel_curve_to(x1, y1, x2, y2, x3, y3)?;
    Ok(ctx)
}

#[pyfunction]
fn rectangle(
    ctx: Py<Canvas>,
    left: f32,
    top: f32,
    width: f32,
    height: f32,
    py: Python<'_>,
) -> Py<Canvas> {
    ctx.bind(py)
        .borrow_mut()
        .rectangle(left, top, width, height);
    ctx
}

#[pyfunction]
fn round_rectangle(
    ctx: Py<Canvas>,
    left: f32,
    top: f32,
    width: f32,
    height: f32,
    py: Python<'_>,
) -> Py<Canvas> {
    ctx.bind(py)
        .borrow_mut()
        .round_rectangle(left, top, width, height);
    ctx
}

#[pyfunction]
fn arc(
    ctx: Py<Canvas>,
    xc: f32,
    yc: f32,
    radius: f32,
    angle1: f32,
    angle2: f32,
    py: Python<'_>,
) -> Py<Canvas> {
    ctx.bind(py)
        .borrow_mut()
        .arc(xc, yc, radius, angle1, angle2);
    ctx
}

#[pyfunction]
fn close_path(ctx: Py<Canvas>, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().close_path();
    ctx
}

#[pyfunction]
#[pyo3(signature = (ctx, r, g, b, a = None))]
fn set_source_rgba(
    ctx: Py<Canvas>,
    r: f32,
    g: f32,
    b: f32,
    a: Option<f32>,
    py: Python<'_>,
) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().set_source_rgba(r, g, b, a);
    ctx
}

#[pyfunction]
fn set_source_rgb(ctx: Py<Canvas>, r: f32, g: f32, b: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py)
        .borrow_mut()
        .set_source_rgba(r, g, b, Some(1.0));
    ctx
}

#[pyfunction]
fn set_line_width(ctx: Py<Canvas>, width: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().set_line_width(width);
    ctx
}

#[pyfunction]
fn set_line_join(ctx: Py<Canvas>, join: LineJoin, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().set_line_join(join);
    ctx
}

#[pyfunction]
#[pyo3(signature = (ctx, dashes, offset = 0.0))]
fn set_dash(ctx: Py<Canvas>, dashes: Vec<f32>, offset: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().set_dash(dashes, offset);
    ctx
}

#[pyfunction]
fn select_font_face(
    ctx: Py<Canvas>,
    family_name: String,
    weight: FontWeight,
    slant: FontSlant,
    py: Python<'_>,
) -> PyResult<Py<Canvas>> {
    ctx.bind(py)
        .borrow_mut()
        .select_font_face(family_name, weight, slant)?;
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
fn show_text(ctx: Py<Canvas>, text: String, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().show_text(text)?;
    Ok(ctx)
}

#[pyfunction]
fn text_extents(
    ctx: Py<Canvas>,
    text: String,
    py: Python<'_>,
) -> PyResult<(f32, f32, f32, f32, f32, f32)> {
    ctx.bind(py).borrow_mut().text_extents(text)
}

#[pyfunction]
fn paint_with_alpha(ctx: Py<Canvas>, a: f32, py: Python<'_>) -> Py<Canvas> {
    ctx.bind(py).borrow_mut().paint_with_alpha(a);
    ctx
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

#[pyfunction]
fn stroke_preserve(ctx: Py<Canvas>, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().stroke_preserve()?;
    Ok(ctx)
}

#[pyfunction]
fn clip_preserve(ctx: Py<Canvas>, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().clip_preserve()?;
    Ok(ctx)
}

#[pyfunction]
fn fill_preserve(ctx: Py<Canvas>, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().fill_preserve()?;
    Ok(ctx)
}

#[pyfunction]
fn add_color_stop_rgba(
    ctx: Py<Canvas>,
    offset: f32,
    r: f32,
    g: f32,
    b: f32,
    a: f32,
    py: Python<'_>,
) -> Py<Canvas> {
    let color4f = Color4f::new(r, g, b, a);
    ctx.bind(py)
        .borrow_mut()
        .add_color_stop_rgba(offset, color4f);
    ctx
}

#[pyfunction]
fn set_source_gradient(ctx: Py<Canvas>, g: Gradient, py: Python<'_>) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().set_source_gradient(g)?;
    Ok(ctx)
}

#[pyfunction]
unsafe fn set_source_image(
    ctx: Py<Canvas>,
    data: Bound<'_, PyByteArray>,
    width: i32,
    height: i32,
    row_bytes: usize,
    x: f32,
    y: f32,
    py: Python<'_>,
) -> PyResult<Py<Canvas>> {
    ctx.bind(py).borrow_mut().set_source_image(
        data.as_bytes_mut(),
        width,
        height,
        row_bytes,
        x,
        y,
    )?;
    Ok(ctx)
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
    fn create(width: i32, height: i32) -> PyResult<Self> {
        Python::attach(|py| {
            let skia_surface = create_skia_surface(width, height)?;
            let canvas = Py::new(
                py,
                Canvas {
                    skia_surface,
                    path: None,
                    font: None,
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

    #[staticmethod]
    unsafe fn create_for_data(
        data: Bound<'_, PyByteArray>,
        width: i32,
        height: i32,
    ) -> PyResult<Self> {
        Python::attach(|py| {
            let skia_surface = create_surface_for_data(data.as_bytes_mut(), width, height)?;
            let canvas = Py::new(
                py,
                Canvas {
                    skia_surface,
                    path: None,
                    font: None,
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
}

#[pymodule]
fn wyvern(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<ImageSurface>()?;
    m.add_class::<LineJoin>()?;
    m.add_class::<FontWeight>()?;
    m.add_class::<FontSlant>()?;
    m.add_class::<Gradient>()?;
    m.add_function(wrap_pyfunction!(save, m)?)?;
    m.add_function(wrap_pyfunction!(restore, m)?)?;
    m.add_function(wrap_pyfunction!(translate, m)?)?;
    m.add_function(wrap_pyfunction!(rotate, m)?)?;
    m.add_function(wrap_pyfunction!(transform, m)?)?;
    m.add_function(wrap_pyfunction!(new_path, m)?)?;
    m.add_function(wrap_pyfunction!(move_to, m)?)?;
    m.add_function(wrap_pyfunction!(line_to, m)?)?;
    m.add_function(wrap_pyfunction!(rel_line_to, m)?)?;
    m.add_function(wrap_pyfunction!(curve_to, m)?)?;
    m.add_function(wrap_pyfunction!(rel_curve_to, m)?)?;
    m.add_function(wrap_pyfunction!(rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(round_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(arc, m)?)?;
    m.add_function(wrap_pyfunction!(close_path, m)?)?;
    m.add_function(wrap_pyfunction!(set_source_rgba, m)?)?;
    m.add_function(wrap_pyfunction!(set_source_rgb, m)?)?;
    m.add_function(wrap_pyfunction!(set_line_width, m)?)?;
    m.add_function(wrap_pyfunction!(set_line_join, m)?)?;
    m.add_function(wrap_pyfunction!(set_dash, m)?)?;
    m.add_function(wrap_pyfunction!(select_font_face, m)?)?;
    m.add_function(wrap_pyfunction!(set_font_size, m)?)?;
    m.add_function(wrap_pyfunction!(text_path, m)?)?;
    m.add_function(wrap_pyfunction!(text_extents, m)?)?;
    m.add_function(wrap_pyfunction!(show_text, m)?)?;
    m.add_function(wrap_pyfunction!(paint_with_alpha, m)?)?;
    m.add_function(wrap_pyfunction!(stroke, m)?)?;
    m.add_function(wrap_pyfunction!(clip, m)?)?;
    m.add_function(wrap_pyfunction!(fill, m)?)?;
    m.add_function(wrap_pyfunction!(stroke_preserve, m)?)?;
    m.add_function(wrap_pyfunction!(clip_preserve, m)?)?;
    m.add_function(wrap_pyfunction!(fill_preserve, m)?)?;
    m.add_function(wrap_pyfunction!(add_color_stop_rgba, m)?)?;
    m.add_function(wrap_pyfunction!(set_source_gradient, m)?)?;
    m.add_function(wrap_pyfunction!(set_source_image, m)?)?;
    Ok(())
}
