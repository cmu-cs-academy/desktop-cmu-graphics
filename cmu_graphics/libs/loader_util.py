import sys
import platform
import struct
import os

def get_platform_string():
    plat = "unsupported"
    if sys.platform == "darwin":
        plat = "mac"
    elif sys.platform == "win32":
        plat = "win"
        n_bits = struct.calcsize("P") * 8
        plat += "_%d" % n_bits
    python_major, python_minor, _ = platform.python_version_tuple()
    plat += "_%s%s" % (python_major, python_minor)
    return plat

def verify_support():
    supported_platforms = [
        'mac_35', 'mac_36', 'mac_37', 'mac_38',
        'win_32_35', 'win_32_36', 'win_32_37', 'win_32_38',
        'win_64_35', 'win_64_36', 'win_64_37', 'win_64_38',
    ]
    if get_platform_string() not in supported_platforms:
        print("""\
Sorry, your operating system or Python version is not currently supported
by CMU Graphics. We support Python 3.5 through Python 3.8 on Windows and
MacOS. You may need to download a newer version of Python to run your
application.""")
        os._exit(1)
