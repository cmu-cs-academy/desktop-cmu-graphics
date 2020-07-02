# setup
source ./helpers/set_python.sh $PYVER
./helpers/setup_build.sh

mkdir pycairo_build || true
source ../venv/bin/activate
cd pycairo

# build the binaries
python3 setup.py sdist bdist_wheel
cd dist

mv *.whl wheel
unzip wheel
cd cairo

# delocate the binaries
soname=$(find *.so)
IFS='.'
read -ra sopieces <<< "$soname"
platform="${sopieces[1]}"
libpath="$platform""_dylibs"

cd ..
delocate-path --lib-path=$libpath cairo
mv cairo/*.so ../../pycairo_build/
mv cairo/$libpath ../../pycairo_build/

# clean up
cd ../../
rm -rf pycairo
rm -rf ../venv

pyenv local system
