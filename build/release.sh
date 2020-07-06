set -e
source env.sh
export zipname=cmu_graphics_installer.zip

cd ../
zip -r $zipname cmu_graphics sample.py

aws s3 cp cmu_graphics_installer.zip $UPLOAD_BUCKET/$zipname

rm cmu_graphics_installer.zip
