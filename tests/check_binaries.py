import importlib.util
import os
import platform
import re
import struct
import subprocess
import sys
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
    # Shipped alongside python.exe by the python.org installer.
    'vcruntime140.dll',
    'vcruntime140_1.dll',
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


def verify_windows_dll_dependencies():
    """
    Check that every DLL cmu_graphics_helpers.pyd imports will actually resolve
    on a student's machine: either Windows/CPython provides it, or we ship it
    next to the .pyd. CPython loads extension modules with
    LOAD_WITH_ALTERED_SEARCH_PATH, so a DLL in that directory is found.
    """
    helpers_dir = find_helpers_dir()
    pyd_path = os.path.join(helpers_dir, 'cmu_graphics_helpers.pyd')
    if not os.path.exists(pyd_path):
        print(f'{pyd_path} does not exist')
        sys.exit(1)

    bundled = {name.lower() for name in os.listdir(helpers_dir) if name.lower().endswith('.dll')}

    missing = [
        dll for dll in imported_dlls(pyd_path)
        if dll not in bundled and not is_always_available(dll)
    ]

    if missing:
        print(
            f'{pyd_path} imports {", ".join(sorted(missing))}, which is neither bundled '
            f'in {helpers_dir} nor guaranteed to exist on a stock Windows machine.\n'
            f'Students without it will get "ImportError: DLL load failed while importing '
            f'cmu_graphics_helpers". Bundle it (see cmu_graphics_helpers/build.rs) or, '
            f'if Windows really does always provide it, add it to ALWAYS_AVAILABLE_DLLS.'
        )
        sys.exit(1)

    print(f'All DLLs imported by {pyd_path} are resolvable.')


def main():
    if platform.system() == 'Windows':
        verify_windows_dll_dependencies()
        return

    if platform.system() != 'Darwin':
        print('Not on a mac or Windows. Skipping ...')
        return
    verify_codesignatures()

if __name__ == '__main__':
    main()

