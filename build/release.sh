set -ex
source env.sh
export zipname=cmu_graphics_installer.zip

cd ../
mkdir cmu_graphics_installer
cp -r cmu_graphics cmu_graphics_installer
cp samples/* cmu_graphics_installer
cp LICENSE cmu_graphics_installer
cp INSTRUCTIONS.pdf cmu_graphics_installer
cd cmu_graphics_installer
zip -rq $zipname *
cd ../

mkdir deploy
cp cmu_graphics_installer/$zipname deploy
cp cmu_graphics/meta/version.txt deploy
rm -r cmu_graphics_installer

if [[ $APPVEYOR ]]; then
  appveyor PushArtifact deploy/cmu_graphics_installer.zip
  appveyor PushArtifact deploy/version.txt
fi

rm -r deploy
