import sys
import struct
import platform
import os
import sysconfig

min_minor_version = 11

def get_platform_string():
    plat = "unsupported"
    if sys.platform == "darwin":
        plat = "mac"
        if platform.machine() == 'arm64':
            plat += '_arm'
    elif sys.platform == "win32":
        plat = "win"
        # sysconfig.get_platform() describes the Python interpreter, so x64
        # Python running under emulation on an ARM computer reports win-amd64
        # and gets the x64 binaries. (Don't use platform.machine(): on Windows
        # it reports the hardware, so it says ARM64 even for emulated x64
        # Python.)
        if sysconfig.get_platform() == "win-arm64":
            plat += "_arm"
        else:
            n_bits = struct.calcsize("P") * 8
            plat += "_%d" % n_bits
    python_major, python_minor, _ = platform.python_version_tuple()
    plat += "_%s%s" % (python_major, python_minor)
    return plat

def verify_os():
    if sys.platform not in ["darwin", "win32"]:
        print("""\
It looks like your computer is using a(n) %(os)s operating system.
%(os)s is not currently supported by CMU Graphics. We support Python 3.%(min_minor_version)d
and higher on Windows and MacOS."""
% {'os': sys.platform, 'min_minor_version': min_minor_version})
        os._exit(1)


def verify_support(vendored):
    python_major, python_minor, _ = platform.python_version_tuple()
    # The vendored distribution only ships binaries for Windows and MacOS.
    if vendored:
        verify_os()

    if python_major != '3':
        print("""\
It looks like you're running a version of Python 2. Since Python 2 is no
longer maintaned as of January 1 2020, CMU Graphics does not support Python 2.
We recommend installing the latest version of Python 3 from python.org""")
        os._exit(1)

    if int(python_minor) < min_minor_version:
        print("""\
It looks like you're running Python 3.%(minor)s. Python 3.%(minor)s is not currently
supported by CMU Graphics. We support Python 3.%(min_minor_version)d and higher. We recommend
installing the latest version of Python 3 from python.org""" %
{"minor": python_minor, 'min_minor_version': min_minor_version})
        os._exit(1)
