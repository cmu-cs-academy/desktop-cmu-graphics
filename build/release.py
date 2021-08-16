# Run me from the root of the repo!

import os
import shutil
import subprocess
from splitversions import split_versions, rm_temp_dirs
from file_io_util import *

VERSION_REGEX=r'version="\d+.\d+.\d+"'

ZIPFILE_NAME = "cmu_graphics_installer.zip"

def make_zip(zip_dest):
    cmd = ["zip", "-rq", f"{zip_dest}/{ZIPFILE_NAME}", ".", "-i", f"{zip_dest}/*"]
    print("Executing command:", " ".join(cmd))
    subprocess.run(cmd)
    # Wait for zip file to be created before exiting function
    while not os.path.exists(f"{zip_dest}/{ZIPFILE_NAME}"):
        pass

def make_deploy_dir(deploy_dest, zip_dest):
    make_all_dirs(deploy_dest)
    for path in [
        f"{zip_dest}/{ZIPFILE_NAME}", 
        "cmu_graphics/meta/version.txt"
        ]:
        shutil.copy2(path, f"{deploy_dest}/{get_filename(path)}")

def main():
    # Update the version inside of setup.py based on version.txt
    version_text = read_file("cmu_graphics/meta/version.txt").strip()
    # TODO: Re-enable this once it's time to upload the actual version
    # replace_file_text("setup.py", VERSION_REGEX, f'version="{version_text}"')

    # Copy all necessary files to zip installer and PyPI installer
    zip_dest = "cmu_graphics_installer"
    # Source code for PyPI version must be in a src/ directory
    pypi_dest= "pypi_upload/src"
    # Files to ignore in the PyPI version (i.e. all the module loaders)
    ignore_fn = shutil.ignore_patterns("*loader", "certifi")
    split_versions(zip_dest, pypi_dest, ignore_fn, "")
    
    make_zip(zip_dest)

    deploy_dest = "deploy"
    make_deploy_dir(deploy_dest, zip_dest)
    
    if "APPVEYOR" in os.environ:
        # Push the zip file to AppVeyor
        for path in os.listdir(deploy_dest):
            artifact_dir = f"deploy/{path}"
            # Path for artifacts is relative to the repo root
            print("Pushing artifact", f"{artifact_dir}...")
            subprocess.run(["appveyor", "PushArtifact", artifact_dir])
        
        # Deploy to PyPI 
        # TODO: Might need to use a different deployment-specific script for this
        # subprocess.run(["source", "helpers/pypi_push.sh"])
    
    rm_temp_dirs(zip_dest, pypi_dest, "", deploy_dest)

main()