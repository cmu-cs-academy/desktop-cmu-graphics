eval "$(pyenv init -)"
if ! pyenv global $1 ; then
    pyenv install $1
    pyenv global $1
fi
