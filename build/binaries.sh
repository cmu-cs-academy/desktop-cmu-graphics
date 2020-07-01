./keys.sh
./helpers/install_global_dependencies.sh

for VERSION in '3.5.4' '3.6.2' '3.7.5' '3.8.1'
do
    export PYVER=$VERSION
    ./helpers/build_pycairo.sh
done

./helpers/upload_binaries.sh
