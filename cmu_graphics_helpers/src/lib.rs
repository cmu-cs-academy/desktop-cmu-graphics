use pyo3::Bound;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyModule;

use geo::BooleanOps;
use geo::{LineString, MultiPolygon, Polygon};

// type aliases
type PyPolygon = Vec<Vec<(f64, f64)>>;
type PyMultiPolygon = Vec<PyPolygon>;

fn to_poly(poly: &PyPolygon) -> Polygon<f64> {
    let mut line_strings: Vec<LineString<_>> = poly
        .clone()
        .into_iter()
        .map(|outline| LineString::from(outline))
        .collect();
    let exterior = line_strings.remove(0);
    Polygon::new(exterior, line_strings)
}

fn from_poly(poly: &Polygon<f64>) -> PyPolygon {
    let holes = poly
        .interiors()
        .iter()
        .map(|hole| hole.points().map(|p| (p.x(), p.y())).collect());
    let mut exterior = vec![poly.exterior().points().map(|p| (p.x(), p.y())).collect()];
    exterior.extend(holes);
    exterior
}

// takes vector of MultiPolygons, returns union of all of them
#[pyfunction]
fn union(ps: Vec<PyMultiPolygon>) -> PyResult<PyMultiPolygon> {
    if ps.len() < 1 {
        return Err(PyValueError::new_err(
            "union must be given at least one MultiPolygon as input",
        ));
    }

    let multis: Option<MultiPolygon<f64>> = ps
        .iter()
        .map(|g| {
            let p = g.iter().map(to_poly).collect();
            MultiPolygon::new(p)
        })
        .collect::<Vec<MultiPolygon<f64>>>()
        .into_iter()
        .reduce(|u, m| m.union(&u));

    let output: PyMultiPolygon = multis.unwrap().0.iter().map(from_poly).collect();

    Ok(output)
}

#[pymodule]
fn cmu_graphics_helpers(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(union, m)?)?;
    Ok(())
}
