set -ex
source env.sh
export zipname=cmu_graphics_installer.zip

cd ../
mkdir cmu_graphics_installer
cp -r cmu_graphics cmu_graphics_installer
cp samples/* cmu_graphics_installer
cd cmu_graphics_installer
zip -rq $zipname *
cd ../

mkdir deploy
cp cmu_graphics_installer/$zipname deploy
cp cmu_graphics/meta/version.txt deploy
rm -r cmu_graphics_installer

python3 -m pip install --upgrade awscli
aws s3 cp deploy/$zipname $UPLOAD_BUCKET/desktop-cmu-graphics/$zipname
aws s3 cp deploy/version.txt $UPLOAD_BUCKET/desktop-cmu-graphics/version.txt
rm -r deploy
