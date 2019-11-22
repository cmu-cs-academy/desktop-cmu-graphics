brew update
brew install pkg-config || brew upgrade pkg-config || true
brew install cairo || brew upgrade cairo || true
brew install pyenv || brew upgrade pyenv || true
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
