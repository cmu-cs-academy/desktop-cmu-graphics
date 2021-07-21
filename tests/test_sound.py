import os
import sys
import argparse
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # pkg-version must be either zip or pip
    parser.add_argument(
        'pkg_version', 
        type=str, 
        help='The specific version of the package (either zip or pip) to test'
    )
    args = parser.parse_args()

if args.pkg_version == "zip":
    from cmu_graphics_installer.cmu_graphics import *
elif args.pkg_version == "pip":
    from pypi_upload.src.cmu_graphics import *
else:
    print(f"""Invalid pkg_version argument: {args.pkg_version}. Please specify 
a package version of either zip or pip.""")
    os._exit(1)

music = Sound('https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/Liberty_bell_march.mp3')
os._exit(0)
