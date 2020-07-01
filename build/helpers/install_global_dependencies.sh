brew update
brew install pkg-config || brew upgrade pkg-config || true
brew install cairo || brew upgrade cairo || true
brew install pyenv || brew upgrade pyenv || true
brew install wget || brew upgrade wget || true
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade awscli
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
