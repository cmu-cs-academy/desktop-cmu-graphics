set -ex
source env.sh
export zipname=cmu_graphics_installer.zip

# Current location: ~

# This part does all the file formatting and ensures that the proper syntax
# goes into the zip and PyPI versions, since they handle imports differently
# and have different OS compatibility
cd cmu_graphics
# Need to overwrite file contents to reflect the proper versions
for filename in *.py
do
  if [[ "$filename" == *.py ]]
  then
    # Remove zip stuff from PyPI version
    sed "$zipregex" $filename > "../pypi_upload/src/cmu_graphics/${filename}"
    # Remove PyPI stuff from zip version
    sed "$pypiregex" $filename > "../cmu_graphics_installer/cmu_graphics/${filename}"
  fi
done
cd libs
for libpath in *
do
  # remove the directories from the PyPI version; they all get pip 
  # installed
  if [[ -d "$libpath" ]]
  then
    rm -r "../../pypi_upload/src/cmu_graphics/libs/${libpath}"
  else
    if [[ "$libpath" == *.py ]]
    then
      sed "$zipregex" $libpath > "../../pypi_upload/src/cmu_graphics/libs/${libpath}"
      sed "$pypiregex" $libpath > "../../cmu_graphics_installer/cmu_graphics/libs/${libpath}"
    fi
  fi
done
cd ../..

cd cmu_graphics_installer
zip -rq $zipname *
cd ../

mkdir deploy
cp cmu_graphics_installer/$zipname deploy
cp cmu_graphics/meta/version.txt deploy
rm -r cmu_graphics_installer

if [[ $APPVEYOR ]]; then
  # Push the zip file to AppVeyor
  appveyor PushArtifact deploy/cmu_graphics_installer.zip
  appveyor PushArtifact deploy/version.txt

  # Deploy to PyPI 
  # TODO: Might need to use a different deployment-specific script for this

  # cd pypi_upload

  # python -m build
  # python -m twine upload dist/*

  # cd ..
fi

rm -r deploy
rm -r pypi_upload
