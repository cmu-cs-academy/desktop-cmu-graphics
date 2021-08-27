import os
import sys
import argparse
import platform
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # pkg-version must be either zip or pip
    parser.add_argument(
        'pkg_version',
        type=str,
        choices=['zip', 'pip'],
        help='The specific version of the package (either zip or pip) to test'
    )
    args = parser.parse_args()
    python_major, python_minor, _ = platform.python_version_tuple()
    pyversion = str(python_major) + str(python_minor)

if args.pkg_version == "zip":
    zip_import_str = f"from cmu_graphics_installer{pyversion}.cmu_graphics import *"
    exec(zip_import_str)
elif args.pkg_version == "pip":
    pip_import_str = f"from pypi_upload{pyversion}.cmu_graphics import *"
    exec(pip_import_str)

music = Sound('https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/Liberty_bell_march.mp3')
os._exit(0)
