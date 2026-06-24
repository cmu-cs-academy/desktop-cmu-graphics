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

#[pymodule]
fn cmu_graphics_helpers(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(union, m)?)?;
    Ok(())
}
