python3 -m pip install --upgrade virtualenv
python3 -m virtualenv ../venv -p python3
source ../venv/bin/activate
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade wheel
python3 -m pip install --upgrade delocate

git clone https://github.com/pygobject/pycairo.git
cd pycairo
git checkout $PYCAIRO_COMMIT
cd ..
