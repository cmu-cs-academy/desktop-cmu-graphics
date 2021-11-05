set -e

source env.sh
./helpers/install_global_dependencies.sh

export PYVER='3.10.0'
./helpers/build_pycairo_modules.sh

python3 ./helpers/replace_images.py
