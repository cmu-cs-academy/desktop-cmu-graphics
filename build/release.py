# Run me from the root of the repo!

import os
import shutil
import subprocess
from splitversions import split_versions, rm_temp_dirs

ZIPFILE_NAME = "cmu_graphics_installer.zip"

def make_zip(zip_dest):
    cmd = ["zip", "-rq", f"{zip_dest}/{ZIPFILE_NAME}", ".", "-i", f"{zip_dest}/*"]
    subprocess.run(cmd, check=True)
    # Wait for zip file to be created before exiting function
    while not os.path.exists(f"{zip_dest}/{ZIPFILE_NAME}"):
        pass

def main():
    zip_dest = "cmu_graphics_installer"
    pypi_dest= "pypi_upload"

    rm_temp_dirs(zip_dest, pypi_dest)

    split_versions(zip_dest, pypi_dest, "")

    make_zip(zip_dest)

    subprocess.run(['python3', '-m', 'build'], cwd=pypi_dest, check=True)
    subprocess.run(['python3', '-m', 'twine', 'upload', '--repository', 'testpypi',
        'dist/*', '-u', '__token__', '-p', os.environ['PYPI_TOKEN']],
        cwd=pypi_dest, check=True)

    # TODO: Upload Zip and version.txt to S3


main()
