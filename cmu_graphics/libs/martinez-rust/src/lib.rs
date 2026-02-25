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

#[pyfunction]
fn union(g1: Vec<Vec<Vec<(f64, f64)>>>, g2: Vec<Vec<Vec<(f64, f64)>>>) -> PyResult<Vec<Vec<Vec<(f64, f64)>>>> {
    let polygons1: Vec<Polygon<f64>> = g1
        .iter()
        .map(to_poly)
        .collect();
    let polygons2: Vec<Polygon<f64>> = g2
        .iter()
        .map(to_poly)
        .collect();

    let multi1 = MultiPolygon::new(polygons1);
    let multi2 = MultiPolygon::new(polygons2);

    let result: MultiPolygon<f64> = multi1.union(&multi2);

    let output: Vec<Vec<Vec<(f64, f64)>>> = result
        .0
        .iter()
        .map(|poly: &Polygon<f64>| {
            let holes = poly.interiors().iter().map(|hole| hole.points().map(|p| (p.x(), p.y())).collect());
            let mut exterior = vec![poly.exterior().points().map(|p| (p.x(), p.y())).collect()];
            exterior.extend(holes);
            exterior
        })
        .collect();

    Ok(output)
}

#[pymodule]
fn martinez(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(union, m)?)?;
    Ok(())
}