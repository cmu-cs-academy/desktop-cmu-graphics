set -e

source env.sh
./helpers/install_global_dependencies.sh

for VERSION in '3.5.4' '3.6.2' '3.7.5' '3.8.1' '3.9.0'
do
    export PYVER=$VERSION
    ./helpers/build_pycairo_binaries.sh
done

./helpers/upload_binaries.sh
