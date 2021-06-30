import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

def check_version(argv):
    if "--version" in argv:
        version_idx = argv.index("--version")
        version = argv[version_idx + 1]
        if version == "zip":
            return "zip"
        elif version == "pip":
            return "pip"
    return None

if check_version(sys.argv) == "zip":
    from cmu_graphics_installer.cmu_graphics import *
elif check_version(sys.argv) == "pip":
    from pypi_upload.src.cmu_graphics import *

music = Sound('https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/Liberty_bell_march.mp3')
os._exit(0)
