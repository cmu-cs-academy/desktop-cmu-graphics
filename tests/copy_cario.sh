pyvershort=$(python print_pyversion_short.py)
pyverlong=$(python print_pyversion_long.py)
toxpkgdir="../.tox/${pyvershort}/lib/${pyverlong}/site-packages/"

# Copying the library manually to every virtual environment because
# Pip can't find the cairo installation from within a virtual environment
cp -r ../cmu_graphics/libs/cairo_loader/modules/cairo_mac/cairo $toxpkgdir