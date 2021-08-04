import shutil
import os
import re
import sys
import platform
from file_io_util import *

# Regex used to remove the zip version code from the pip version and vice versa
ZIP_REGEX=r"### ZIPFILE VERSION ###.*?### END ZIPFILE VERSION ###"
PYPI_REGEX=r"### PYPI VERSION ###.*?### END PYPI VERSION ###"

def split_versions(zip_dest, pypi_dest, ignore_fn):
    make_all_dirs(zip_dest, pypi_dest)
    
    # cmu_graphics package
    print("Copying cmu_graphics package to pypi_upload/src/ ...")
    shutil.copytree("cmu_graphics", f"{pypi_dest}/cmu_graphics", ignore=ignore_fn)
    print("Copying cmu_graphics package to cmu_graphics_installer/ ...")
    shutil.copytree("cmu_graphics", f"{zip_dest}/cmu_graphics")
    # sample files
    print("Copying sample files to pypi_upload/src/cmu_graphics ...")
    shutil.copytree("samples", f"{pypi_dest}/cmu_graphics/samples")
    print("Copying sample files to pypi_upload/src/cmu_graphics ...")
    for sample_path in os.listdir("samples"):
        shutil.copy2(f"samples/{sample_path}", f"{zip_dest}/cmu_graphics/{sample_path}")
    # Meta files and docs
    for path in ["LICENSE", "INSTRUCTIONS.pdf"]:
        shutil.copy2(path, f"{zip_dest}/{get_filename(path)}")
    pypi_parent = "/".join(pypi_dest.split("/")[:-1])
    for path in ["LICENSE", "README.md", "setup.py", "pyproject.toml"]:
        shutil.copy2(path, f"{pypi_parent}/{get_filename(path)}") 
        # Note that those files are in a different location than src, where the
        # actual package is

    # Separate the PyPI and zip versions of cmu_graphics from each other
    pypi_source_dirs = [
        f"{pypi_dest}/cmu_graphics",
        f"{pypi_dest}/cmu_graphics/libs"
        ]
    for dir in pypi_source_dirs:
        for path in os.listdir(dir):
            full_path = f"{dir}/{path}"
            if os.path.isfile(full_path):
                replace_file_text(full_path, ZIP_REGEX, "", re.DOTALL)
    zip_source_dirs = [
        f"{zip_dest}/cmu_graphics",
        f"{zip_dest}/cmu_graphics/libs"
        ]
    for dir in zip_source_dirs:
        for path in os.listdir(dir):
            full_path = f"{dir}/{path}"
            if os.path.isfile(full_path):
                replace_file_text(full_path, PYPI_REGEX, "", re.DOTALL)

def rm_temp_dirs(zip_dest, pypi_dest, deploy_dest = None):
    shutil.rmtree(zip_dest)
    shutil.rmtree(pypi_dest)
    if deploy_dest != None:
        shutil.rmtree(deploy_dest)

def main(argv):
    if "--mode" in argv:
        mode_idx = argv.index("--mode")
        mode = argv[mode_idx + 1]

        python_major, python_minor, _ = platform.python_version_tuple()
        python_str = f"{python_major}{python_minor}"

        zip_dest = "cmu_graphics_installer" + python_str
        pypi_dest= f"pypi_upload{python_str}/src"
        if mode == "split":
            print("""Manually splitting the zip and pip versions of CMU
Graphics. Please make sure to re-run this command with the 'clean' flag to 
remove the temporary files.""")
            ignore_fn = shutil.ignore_patterns("*loader", "certifi")
            split_versions(zip_dest, pypi_dest, ignore_fn)
            os._exit(0)
        elif mode == "clean":
            pypi_dest = "pypi_upload" + python_str
            print("Cleaning up temporary zip and pip versions of CMU Graphics...", end="")
            rm_temp_dirs(zip_dest, pypi_dest)
            print("Done!")
            os._exit(0)
        else:
            print("Invalid mode: choose one of 'split' or 'clean'")
            os._exit(1)
    print("Error: please run splitversions.py using a '--mode' flag of 'split' or 'clean'")
    os._exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])