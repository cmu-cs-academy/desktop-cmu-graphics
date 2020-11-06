# setup
source ./helpers/set_python.sh $PYVER
./helpers/setup_build.sh

source ../venv/bin/activate
cd pycairo

# build the module
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

mkdir ../../../cmu_graphics/libs/cairo_loader/modules || true
rm -rf ../../../cmu_graphics/libs/cairo_loader/modules/cairo_mac/cairo
mv cairo ../../../cmu_graphics/libs/cairo_loader/modules/cairo_mac/

# clean up
cd ../../
rm -rf pycairo
rm -rf ../venv

pyenv global system
