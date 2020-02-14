export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
# pyenv install $PYVER
# eval "$(pyenv init -)"
# pyenv global $PYVER
python3 -m pip install virtualenv
python3 -m virtualenv ../venv -p python3
source ../venv/bin/activate
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade wheel
python3 -m pip install --upgrade delocate
git clone https://github.com/pygobject/pycairo.git
