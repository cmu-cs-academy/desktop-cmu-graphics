set -ex
source env.sh
export zipname=cmu_graphics_installer.zip

cd ../
mkdir cmu_graphics_installer
cp -r cmu_graphics cmu_graphics_installer
cp samples/* cmu_graphics_installer
cd cmu_graphics_installer
zip -r $zipname *
cd ../

mkdir deploy
cp cmu_graphics_installer/$zipname deploy
cp cmu_graphics/meta/version.txt deploy
rm -r cmu_graphics_installer

export tag_version=$(git tag --points-at HEAD)
export txt_version=$(cat cmu_graphics/meta/version.txt)

if [[ $tag_version != $txt_version ]]; then
  echo "Git tag does not match version txt"
  exit 1;
fi
