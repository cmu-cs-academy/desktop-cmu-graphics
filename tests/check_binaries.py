import argparse
import importlib.util
import os
import platform
import re
import struct
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

def is_properly_signed(path):
    try:
        result_bytes = subprocess.check_output(
            [
                'codesign',
                '-dv',
                '--verbose=4',
                path,
            ],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError:
        return False

    result_lines = result_bytes.decode('iso-8859-1').splitlines()
    if 'Authority=Developer ID Application: Evan Mallory (LXH25PRRZ2)' not in result_lines:
        return False

    return True

def has_correct_architecture(path):
    is_arm = 'mac_arm' in path
    is_x86 = not is_arm

    result_bytes = subprocess.check_output(['file', path])
    result = result_bytes.decode('iso-8859-1')

    if is_x86 and not 'x86_64' in result:
        return False

    if is_arm and not 'arm64' in result:
        return False

    return True

def verify_codesignatures():
    # tox only runs this in the zip envs, from {envtmpdir}, where
    # tests/install.py has unpacked the installer into ./cmu_graphics.
    base_path = 'cmu_graphics'

    success = True
    checked = 0
    for path, _, files in os.walk(base_path):
        for filename in files:
            _, extension = os.path.splitext(filename)
            if extension in ('.so', '.dylib'):
                filepath = os.path.abspath(os.path.join(path, filename))
                checked += 1
                if not is_properly_signed(filepath):
                    print(f'{filepath} was not appropriately signed')
                    success = False

                if not has_correct_architecture(filepath):
                    print(f'{filepath} does not have the correct architecture')
                    success = False

    # Guard against this check silently passing because it was looking in the
    # wrong place, which is how it went unnoticed that for a long time it
    # checked nothing at all.
    if checked == 0:
        sys.exit(f'no .so or .dylib files were found under '
                 f'{os.path.abspath(base_path)}')

    print(f'Checked {checked} binaries.')
    if not success:
        sys.exit(1)


# DLLs that Windows itself, or the CPython installation, always provides. Anything
# cmu_graphics_helpers.pyd imports that is not on this list has to be shipped inside
# the package directory, next to the .pyd, or students hit
# "ImportError: DLL load failed" on machines that happen not to have it.
#
# MSVCP140.dll is deliberately absent here: it is the C++ standard library, it comes
# only from the Visual C++ Redistributable, and it is not present on a stock Windows
# machine. cmu_graphics_helpers/build.rs bundles it into the wheel; this check is
# what keeps that from silently regressing.
ALWAYS_AVAILABLE_DLLS = {
    'advapi32.dll',
    'bcrypt.dll',
    'bcryptprimitives.dll',
    'gdi32.dll',
    'kernel32.dll',
    'ntdll.dll',
    'ole32.dll',
    'opengl32.dll',
    'shell32.dll',
    'user32.dll',
    'ucrtbase.dll',
    # Shipped alongside python.exe by the python.org installer. We bundle our
    # own copy too, so this only matters if that bundling is ever dropped.
    'vcruntime140.dll',
}


def is_always_available(dll_name):
    # api-ms-win-* are the UCRT/OS API sets, resolved by Windows itself, and
    # python3.dll / python3NN.dll come from the interpreter that is running us.
    return (
        dll_name in ALWAYS_AVAILABLE_DLLS
        or dll_name.startswith('api-ms-win-')
        or re.fullmatch(r'python3[0-9]*\.dll', dll_name) is not None
    )


def imported_dlls(path):
    """The DLL names in a PE file's import table, lowercased."""
    data = Path(path).read_bytes()
    pe_offset = struct.unpack_from('<I', data, 0x3C)[0]
    if data[pe_offset:pe_offset + 4] != b'PE\0\0':
        raise ValueError(f'{path} is not a PE file')

    n_sections = struct.unpack_from('<H', data, pe_offset + 6)[0]
    optional_size = struct.unpack_from('<H', data, pe_offset + 20)[0]
    optional_offset = pe_offset + 24
    is_pe32_plus = struct.unpack_from('<H', data, optional_offset)[0] == 0x20B

    # The import table is the second entry in the data directory, which follows
    # the optional header's fixed fields (112 bytes for PE32+, 96 for PE32).
    data_directory = optional_offset + (112 if is_pe32_plus else 96)
    import_rva = struct.unpack_from('<I', data, data_directory + 8)[0]

    sections = []
    section_offset = optional_offset + optional_size
    for i in range(n_sections):
        header = data[section_offset + i * 40:section_offset + (i + 1) * 40]
        virtual_size, virtual_address, raw_size, raw_offset = struct.unpack_from('<IIII', header, 8)
        sections.append((virtual_address, max(virtual_size, raw_size), raw_offset))

    def to_offset(rva):
        for virtual_address, size, raw_offset in sections:
            if virtual_address <= rva < virtual_address + size:
                return raw_offset + (rva - virtual_address)
        raise ValueError(f'RVA {rva:#x} is outside every section of {path}')

    def read_string(offset):
        return data[offset:data.index(b'\0', offset)].decode('ascii')

    names = []
    offset = to_offset(import_rva)
    while True:
        # Each import descriptor is 20 bytes, terminated by an all-zero one.
        descriptor = data[offset:offset + 20]
        if len(descriptor) < 20 or descriptor == b'\0' * 20:
            break
        name_rva = struct.unpack_from('<I', descriptor, 12)[0]
        if name_rva == 0:
            break
        names.append(read_string(to_offset(name_rva)).lower())
        offset += 20
    return names


def find_helpers_dir():
    """
    The directory holding cmu_graphics_helpers.pyd, for whichever distribution
    is installed: site-packages for the pip install, the vendored module
    directory under cmu_graphics/libs for the zip install.
    """
    spec = importlib.util.find_spec('cmu_graphics_helpers')
    if spec is not None and spec.origin is not None:
        return os.path.dirname(spec.origin)

    spec = importlib.util.find_spec('cmu_graphics')
    if spec is None or spec.origin is None:
        print('neither cmu_graphics_helpers nor cmu_graphics could be found')
        sys.exit(1)

    return os.path.join(
        os.path.dirname(spec.origin),
        'libs', 'cmu_graphics_helpers_loader', 'modules',
        'cmu_graphics_helpers_win_64', 'cmu_graphics_helpers',
    )


def verify_windows_dll_dependencies(helpers_dir, source=None):
    """
    Check that every DLL needed to import cmu_graphics_helpers will actually
    resolve on a student's machine: either Windows/CPython provides it, or we
    ship it next to the .pyd. CPython loads extension modules with
    LOAD_WITH_ALTERED_SEARCH_PATH, so a DLL in that directory is found.

    This walks dependencies transitively, not just the .pyd's own imports. That
    matters: the .pyd does not import vcruntime140_1.dll, but the msvcp140.dll we
    bundle does, so bundling msvcp140.dll alone would still fail to load on a
    machine without the Visual C++ Redistributable.
    """
    # When checking an unpacked wheel, name the wheel in any error rather than
    # the temporary directory it happens to be unpacked into.
    source = source or helpers_dir
    pyd_path = os.path.join(helpers_dir, 'cmu_graphics_helpers.pyd')
    if not os.path.exists(pyd_path):
        print(f'{pyd_path} does not exist')
        sys.exit(1)

    bundled = {
        name.lower(): os.path.join(helpers_dir, name)
        for name in os.listdir(helpers_dir)
        if name.lower().endswith('.dll')
    }

    # Breadth-first over everything that has to load, starting at the .pyd and
    # following into each bundled DLL we find along the way.
    missing = {}
    inspected = set()
    queue = [('cmu_graphics_helpers.pyd', pyd_path)]
    while queue:
        needed_by, path = queue.pop(0)
        inspected.add(needed_by.lower())
        for dll in imported_dlls(path):
            if dll in bundled:
                if dll not in inspected:
                    inspected.add(dll)
                    queue.append((dll, bundled[dll]))
            elif not is_always_available(dll):
                missing.setdefault(dll, needed_by)

    if missing:
        for dll, needed_by in sorted(missing.items()):
            print(
                f'{needed_by} imports {dll}, which is neither bundled in {source} '
                f'nor guaranteed to exist on a stock Windows machine.'
            )
        print(
            f'\nStudents without it will get "ImportError: DLL load failed while importing '
            f'cmu_graphics_helpers". Bundle it (add it to DLL_NAMES in '
            f'cmu_graphics_helpers/build.rs) or, if Windows really does always provide it, '
            f'add it to ALWAYS_AVAILABLE_DLLS.'
        )
        sys.exit(1)

    checked = ', '.join(sorted(inspected))
    print(f'All DLLs needed to import cmu_graphics_helpers are resolvable ({checked}).')


def verify_wheel(wheel):
    """
    Run the same dependency check against a freshly built wheel, before it is
    installed anywhere.
    """
    wheel_path = Path(wheel)
    if wheel_path.is_dir():
        wheels = sorted(wheel_path.glob('*win_amd64.whl'), key=lambda p: p.stat().st_mtime)
        if not wheels:
            print(f'no win_amd64 wheel found in {wheel_path}')
            sys.exit(1)
        wheel_path = wheels[-1]
    print(f'Checking {wheel_path.name}')

    with tempfile.TemporaryDirectory() as unpacked:
        with zipfile.ZipFile(wheel_path) as zf:
            zf.extractall(unpacked)
        verify_windows_dll_dependencies(
            os.path.join(unpacked, 'cmu_graphics_helpers'), source=wheel_path.name
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--wheel',
        help='check a built Windows wheel (or a directory holding one) instead of '
             'whichever cmu_graphics_helpers is installed',
    )
    args = parser.parse_args()

    if args.wheel:
        verify_wheel(args.wheel)
        return

    if platform.system() == 'Windows':
        verify_windows_dll_dependencies(find_helpers_dir())
        return

    if platform.system() != 'Darwin':
        print('Not on a mac or Windows. Skipping ...')
        return
    verify_codesignatures()

if __name__ == '__main__':
    main()
