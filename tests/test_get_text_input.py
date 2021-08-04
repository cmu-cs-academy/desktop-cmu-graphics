# Exits with a 0 return code if the text input modal opens without errors
# within 5 seconds. Exits with a 1 return code otherwise.

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import psutil
import time
from datetime import datetime, timedelta
from threading import Thread
import argparse
import platform

args = pyversion = None
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # pkg_version must be either zip or pip
    parser.add_argument(
        'pkg_version', 
        type=str, 
        help='The specific version of the package (either zip or pip) to test'
    )
    args = parser.parse_args()
    python_major, python_minor, _ = platform.python_version_tuple()
    pyversion = str(python_major) + str(python_minor)

if args.pkg_version == "zip":
    zip_import_str = f"from cmu_graphics_installer{pyversion}.cmu_graphics import *"
    exec(zip_import_str)
elif args.pkg_version == "pip":
    pip_import_str = f"from pypi_upload{pyversion}.src.cmu_graphics import *"
    exec(pip_import_str)
else:
    print(f"""Invalid pkg_version argument: {args.pkg_version}. Please specify 
a package version of either zip or pip.""")
    os._exit(1)

def get_children_pids():
    return {child.pid for child in psutil.Process().children(recursive=True)}

def wait_for_modal(initial_children_pids):
    try:
        time.sleep(1)
        start_time = datetime.now()
        while True:
            if datetime.now() - start_time > timedelta(seconds=5):
                os._exit(1)
            current_children_pids = get_children_pids()
            if len(current_children_pids) > len(initial_children_pids):
                modal_pid = list(current_children_pids - initial_children_pids)[0]
                psutil.Process(modal_pid).terminate()
                os._exit(0)
    except:
        os._exit(1)

def onStep():
    Thread(target=wait_for_modal, args=(get_children_pids(),)).start()
    app.getTextInput()

cmu_graphics.loop()
