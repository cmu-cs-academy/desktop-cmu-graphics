export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"

mkdir release || true

source ../venv/bin/activate
python3 --version

cd pycairo
git checkout $PYCAIRO_COMMIT

python3 setup.py sdist bdist_wheel
cd dist

mv *.whl wheel
unzip wheel
cd cairo
rm *.so
wget https://s3.amazonaws.com/cmu-cs-academy.lib.prod/cpython-cmu-graphics-binaries/binaries.tgz
tar -xvf binaries.tgz
rm binaries.tgz
cd ..

mkdir ../../cmu_graphics/cairo/modules || true
mv cairo ../../cmu_graphics/cairo/modules/cairo_mac

cd ../../
mkdir cmu_graphics_installer
mv cmu_graphics cmu_graphics_installer
mv sample.py cmu_graphics_installer
zip -r cmu_graphics_installer.zip cmu_graphics_installer
mv cmu_graphics_installer.zip release
