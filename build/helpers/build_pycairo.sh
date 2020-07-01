# set up the correct python version
eval "$(pyenv init -)"
if ! pyenv global $PYVER ; then
    pyenv install $PYVER
    pyenv global $PYVER
fi

# install dependencies and set up the environment
python3 -m pip install virtualenv
python3 -m virtualenv ../venv -p python3
source ../venv/bin/activate
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade wheel
python3 -m pip install --upgrade delocate

git clone https://github.com/pygobject/pycairo.git

mkdir pycairo_build || true

source ../venv/bin/activate
python3 --version

cd pycairo
git checkout $PYCAIRO_COMMIT

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
