import argparse
import os
import platform
import re
import shutil

# Regex used to remove the zip version code from the pip version and vice versa
ZIP_REGEX=r"### ZIPFILE VERSION ###.*?### END ZIPFILE VERSION ###"
PYPI_REGEX=r"### PYPI VERSION ###.*?### END PYPI VERSION ###"

def replace_file_text(path, regex, repl, flags=0):
    old_text = ""
    with open(path, "r", encoding="utf-8") as f:
        old_text = f.read()

    new_text = re.sub(regex, repl, old_text, flags=flags)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

def make_all_dirs(*dirs):
    for dir in dirs:
        os.makedirs(dir)

def apply_regex_to_dirs(dirs, regex):
    for dir in dirs:
        for path in os.listdir(dir):
            full_path = f"{dir}/{path}"
            if full_path.endswith('.py') and os.path.isfile(full_path):
                replace_file_text(full_path, regex, "", re.DOTALL)


def split_versions(zip_dest, pypi_dest, dots):
    make_all_dirs(dots + zip_dest, dots + pypi_dest)

    print(f"Copying cmu_graphics package to {pypi_dest} ...")
    shutil.copytree(dots + "cmu_graphics", dots + f"{pypi_dest}/cmu_graphics",
        ignore=shutil.ignore_patterns("*loader", "certifi"))
    print(f"Copying cmu_graphics package to {zip_dest} ...")
    shutil.copytree(dots + "cmu_graphics", dots + f"{zip_dest}/cmu_graphics")

    print(f"Copying sample files to {pypi_dest}/cmu_graphics ...")
    shutil.copytree(dots + "samples", dots + f"{pypi_dest}/cmu_graphics/samples")
    print(f"Copying sample files to {zip_dest} ...")
    shutil.copytree(dots + "samples", dots + f"{zip_dest}/samples")

    # Meta files and docs
    for path in ["LICENSE", "INSTRUCTIONS.pdf"]:
        shutil.copy2(dots + path, dots + f"{zip_dest}/{os.path.basename(path)}")
    for path in ["LICENSE", "README.md", "setup.py", "pyproject.toml"]:
        shutil.copy2(dots + path, dots + f"{pypi_dest}/{os.path.basename(path)}")

    apply_regex_to_dirs([
        dots + f"{pypi_dest}/cmu_graphics",
        dots + f"{pypi_dest}/cmu_graphics/libs"
        ],
        ZIP_REGEX)

    apply_regex_to_dirs([
        dots + f"{zip_dest}/cmu_graphics",
        dots + f"{zip_dest}/cmu_graphics/libs"
        ], PYPI_REGEX)


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
