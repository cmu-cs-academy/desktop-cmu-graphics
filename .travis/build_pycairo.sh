export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"

mkdir build || true

source ../venv/bin/activate
python3 --version

cd pycairo
git checkout 06a76dc704fad9aea046ea5ddb658ff3dc4521b2

python3 setup.py sdist bdist_wheel
cd dist

mv *.whl wheel
unzip wheel
cd cairo

soname=$(find *.so)
IFS='.'
read -ra sopieces <<< "$soname"
platform="${sopieces[1]}"
libpath="$platform""_dylibs"

cd ..
delocate-path --lib-path=$libpath cairo
mv cairo/*.so ../../build/
mv cairo/$libpath ../../build/

cd ../../
rm -rf pycairo
rm -rf ../venv
