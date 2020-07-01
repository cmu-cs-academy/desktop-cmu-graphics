cd pycairo_build
tar -zcvf binaries.tgz .
aws s3 cp binaries.tgz $UPLOAD_BUCKET/binaries.tgz
cd ..
rm -rf pycairo_build
rm .python-version
