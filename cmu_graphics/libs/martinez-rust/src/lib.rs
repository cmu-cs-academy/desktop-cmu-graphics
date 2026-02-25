use pyo3::prelude::*;
use pyo3::types::PyModule;
use pyo3::Bound;

use geo::algorithm::unary_union;
use geo_types::{LineString, Polygon, MultiPolygon};

#[pyfunction]
fn union(l: Vec<Vec<Vec<(f64, f64)>>>) -> PyResult<Vec<Vec<Vec<(f64, f64)>>>> {
    let polygons: Vec<Polygon<f64>> = l
        .iter()
        .map(|poly| {
            let mut line_strings : Vec<LineString<_>> = poly.clone().into_iter().map(|outline| LineString::from(outline)).collect();
            let exterior = line_strings.remove(0);
            Polygon::new(exterior, line_strings)
        })
        .collect();

    let multi = MultiPolygon(polygons);

    let result: MultiPolygon<f64> = unary_union(&multi);

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