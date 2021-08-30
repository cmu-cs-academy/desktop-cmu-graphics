# Run me from the root of the repo!

import argparse
import os
import shutil
import sys
import subprocess
from splitversions import split_versions, rm_temp_dirs

ZIPFILE_NAME = "cmu_graphics_installer.zip"

parser = argparse.ArgumentParser()
parser.add_argument("--publish", action="store_true")
args = parser.parse_args()

def make_zip(zip_dest):
    cmd = f"{sys.executable} -m zipfile -c {ZIPFILE_NAME} {zip_dest}"
    subprocess.run(cmd, check=True, shell=True)
    # Wait for zip file to be created before exiting function
    while not os.path.exists(ZIPFILE_NAME):
        pass

def main():
    zip_dest = "cmu_graphics_installer"
    pypi_dest= "pypi_upload"

    rm_temp_dirs(zip_dest, pypi_dest)

    split_versions(zip_dest, pypi_dest, "")

    make_zip(zip_dest)

    subprocess.run(['python3', '-m', 'build'], cwd=pypi_dest, check=True)

    if args.publish:
        subprocess.run(['python3', '-m', 'twine', 'upload', '--repository', 'testpypi',
            'dist/*', '-u', '__token__', '-p', os.environ['PYPI_TEST_TOKEN']],
            cwd=pypi_dest, check=True)

        s3_dest = 's3://cmu-cs-academy.lib.prod/desktop-cmu-graphics-test/'
        subprocess.run(['aws', 's3', 'cp', zip_dest + '/cmu_graphics/meta/version.txt',
            s3_dest], check=True)
        subprocess.run(['aws', 's3', 'cp', ZIPFILE_NAME, s3_dest], check=True)

main()
