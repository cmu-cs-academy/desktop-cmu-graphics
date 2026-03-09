use pyo3::prelude::*;
use pyo3::types::PyModule;
use pyo3::Bound;

use geo::BooleanOps;
use geo::{LineString, Polygon, MultiPolygon};

fn to_poly(poly : &Vec<Vec<(f64, f64)>>) -> Polygon<f64> {
    let mut line_strings : Vec<LineString<_>> = poly.clone().into_iter().map(|outline| LineString::from(outline)).collect();
    let exterior = line_strings.remove(0);
    Polygon::new(exterior, line_strings)
}

fn from_poly(poly : &Polygon<f64>) -> Vec<Vec<(f64, f64)>> {
    let holes = poly.interiors().iter().map(|hole| hole.points().map(|p| (p.x(), p.y())).collect());
    let mut exterior = vec![poly.exterior().points().map(|p| (p.x(), p.y())).collect()];
    exterior.extend(holes);
    exterior
}

// takes vector of MultiPolygons, returns union of all of them
#[pyfunction]
fn union(ps: Vec<Vec<Vec<Vec<(f64, f64)>>>>) -> PyResult<Vec<Vec<Vec<(f64, f64)>>>> {
    let multis: Vec<MultiPolygon<f64>> = ps
        .iter()
        .map(|g| {
            let p = g.iter().map(to_poly).collect();
            MultiPolygon::new(p)
                 })
        .collect();

    let result: MultiPolygon<f64> = multis
        .clone()
        .into_iter()
        .fold(multis[0].clone(), |u, m| m.union(&u));

    let output: Vec<Vec<Vec<(f64, f64)>>> = result
        .0
        .iter()
        .map(from_poly)
        .collect();

    Ok(output)
}

#[pymodule]
fn cmu_graphics_helpers(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(union, m)?)?;
    Ok(())
}