set -ex
source env.sh
export zipname=cmu_graphics_installer.zip
# Regex used to remove the zip version code from the pip version and vice versa
zipregex="/### ZIPFILE VERSION ###/,/### END ZIPFILE VERSION ###/d"
pypiregex="/### PYPI VERSION ###/,/### END PYPI VERSION ###/d"

cd ..
mkdir cmu_graphics_installer pypi_upload
# Source code for PyPI version must be in a src/ directory
mkdir pypi_upload/src
for dir in cmu_graphics_installer pypi_upload/src
do
  cp -r cmu_graphics $dir
done

cp samples/* cmu_graphics_installer
# sample files must be included in the PyPI package itself
cp -r samples pypi_upload/src/cmu_graphics

cp LICENSE INSTRUCTIONS.pdf cmu_graphics_installer
cp LICENSE README.md setup.py pyproject.toml pypi_upload

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

# Update the version inside of setup.py
# TODO: Re-enable this once it's time to upload the actual version
# TODO: I actually probably need to move this to the beginning of the script
# versionregex="[0123456789]+.[0123456789]+.[0123456789]+"
# match=$(grep -E ${versionregex} cmu_graphics/meta/version.txt)
# pattern="s/version=\"${versionregex}\"/version=\"${match}\"/"
# sed -i -E "$pattern" setup.py

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
