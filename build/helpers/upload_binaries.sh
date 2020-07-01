cd pycairo_build
tar -zcvf binaries.tgz .
aws s3 cp binaries.tgz s3://cmu-cs-academy.lib.prod/cpython-cmu-graphics-binaries/binaries.tgz
cd ..
rm -rf pycairo_build
