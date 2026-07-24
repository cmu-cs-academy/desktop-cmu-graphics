import argparse
import os
import platform
import re
import shutil

def make_all_dirs(*dirs):
    for dir in dirs:
        os.makedirs(dir)

def set_vendored(dist_py_path, vendored):
    # Bake the distribution switch (see cmu_graphics/_dist.py) into a build
    # copy. The source is checked in as VENDORED = True (used by the zip
    # installer and local development); this flips it for the pip build.
    with open(dist_py_path, "r", encoding="utf-8") as f:
        old_text = f.read()

    new_text, n = re.subn(
        r"^VENDORED = .*$", f"VENDORED = {vendored}", old_text, flags=re.MULTILINE)
    if n != 1:
        raise Exception(
            f"Expected exactly one 'VENDORED =' line in {dist_py_path}, found {n}")

    with open(dist_py_path, "w", encoding="utf-8") as f:
        f.write(new_text)


def split_versions(zip_dest, pypi_dest, dots):
    make_all_dirs(dots + zip_dest, dots + pypi_dest)

    print(f"Copying cmu_graphics package to {pypi_dest} ...")
    shutil.copytree(dots + "cmu_graphics", dots + f"{pypi_dest}/cmu_graphics",
        ignore=shutil.ignore_patterns("*loader", "certifi"))
    print(f"Copying cmu_graphics package to {zip_dest} ...")
    shutil.copytree(dots + "cmu_graphics", dots + f"{zip_dest}/cmu_graphics")

    print(f"Copying cmu_cpcs_utils to {pypi_dest} ...")
    shutil.copy(dots + "cmu_cpcs_utils.py", dots + f"{pypi_dest}/")
    print(f"Copying cmu_cpcs_utils to {zip_dest} ...")
    shutil.copy(dots + "cmu_cpcs_utils.py", dots + f"{zip_dest}/")

    print(f"Copying sample files to {pypi_dest}/cmu_graphics ...")
    shutil.copytree(dots + "samples", dots + f"{pypi_dest}/cmu_graphics/samples")
    print(f"Copying sample files to {zip_dest} ...")
    shutil.copytree(dots + "samples", dots + f"{zip_dest}/samples")

    # Meta files and docs
    for path in ["LICENSE", "INSTRUCTIONS.pdf"]:
        shutil.copy2(dots + path, dots + f"{zip_dest}/{os.path.basename(path)}")
    for path in ["LICENSE", "README.md", "pyproject.toml"]:
        shutil.copy2(dots + path, dots + f"{pypi_dest}/{os.path.basename(path)}")

    # The zip copy keeps the checked-in VENDORED = True; only the pip copy
    # needs flipping to load dependencies from the system instead of libs.
    set_vendored(dots + f"{pypi_dest}/cmu_graphics/_dist.py", False)


def rm_temp_dirs(zip_dest, pypi_dest, dots=''):
    for path in [dots + zip_dest, dots + pypi_dest]:
        if os.path.exists(path):
            shutil.rmtree(path)


def main(args):
    python_str = ""
    root_dir = ""
    if args.location == 'tests':
        python_major, python_minor, _ = platform.python_version_tuple()
        python_str = f"{python_major}{python_minor}"
        root_dir = "../"

    zip_dest = "cmu_graphics_installer" + python_str
    pypi_dest= f"pypi_upload{python_str}"
    if args.mode == "split":
        print("""Manually splitting the zip and pip versions of CMU
Graphics. Please make sure to re-run this command with the 'clean' flag to
remove the temporary files.""")
        split_versions(zip_dest, pypi_dest, root_dir)
    elif args.mode == "clean":
        print("Cleaning up temporary zip and pip versions of CMU Graphics...", end="")
        rm_temp_dirs(zip_dest, pypi_dest, root_dir)
        print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # mode must be split or clean
    parser.add_argument(
        'mode',
        type=str,
        choices=['split', 'clean'],
        help='Specifies whether to create or delete the test files'
    )
    # location must be root or tests
    parser.add_argument(
        'location',
        type=str,
        choices=['root', 'tests'],
        help='The location in which the file creation/deletion is happening'
    )
    main(parser.parse_args())
