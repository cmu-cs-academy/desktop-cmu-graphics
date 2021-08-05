import platform
import shutil
import os

def main():
    python_major, python_minor, _ = platform.python_version_tuple()
    short_pyversion = f"py{str(python_major)}{str(python_minor)}"
    long_pyversion = f"python{str(python_major)}.{str(python_minor)}"
    cairo_dir="../cmu_graphics/libs/cairo_loader/modules/cairo_mac/cairo/"
    tox_lib_dir=f"../.tox/{short_pyversion}/lib/{long_pyversion}/site-packages/cairo"
    if (not os.path.exists(tox_lib_dir)):
        shutil.copytree(cairo_dir, tox_lib_dir)

if __name__ == "__main__":
    main()