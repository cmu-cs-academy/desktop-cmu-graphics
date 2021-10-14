# Run me from the root of the repo!

import argparse
import os
import sys
import subprocess
from splitversions import split_versions, rm_temp_dirs

parser = argparse.ArgumentParser()
parser.add_argument("--publish", action="store_true")
parser.add_argument("--prod", action="store_true")
args = parser.parse_args()

def main():
    zip_dest = "cmu_graphics_installer"
    pypi_dest= "pypi_upload"

    rm_temp_dirs(zip_dest, pypi_dest)
    split_versions(zip_dest, pypi_dest, "")

    zipfile_name = "cmu_graphics_installer.zip"
    subprocess.run([sys.executable, '-m', 'zipfile', '-c', zipfile_name, zip_dest],
        check=True)
    subprocess.run([sys.executable, '-m', 'build'], cwd=pypi_dest, check=True)

    if args.publish:
        pypi_repo_args = [] if args.prod else ['--repository', 'testpypi']

        subprocess.run([sys.executable, '-m', 'twine', 'upload',
            'dist/*', '-u', '__token__', '-p', os.environ['PYPI_TOKEN' if args.prod else 'PYPI_TEST_TOKEN']] + pypi_repo_args,
            cwd=pypi_dest, check=True)

        s3_dest = ('s3://cmu-cs-academy.lib.prod/desktop-cmu-graphics-test/' if args.test else
            's3://cmu-cs-academy.lib.prod/desktop-cmu-graphics/')
        subprocess.run(['aws', 's3', 'cp', zip_dest + '/cmu_graphics/meta/version.txt',
            s3_dest], check=True)
        subprocess.run(['aws', 's3', 'cp', zipfile_name, s3_dest], check=True)

main()
