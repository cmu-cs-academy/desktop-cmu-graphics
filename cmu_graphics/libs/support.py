import sys
import platform
import os

min_minor_version = 11

def verify_os():
    if sys.platform not in ["darwin", "win32"]:
        print("""\
It looks like your computer is using a(n) %(os)s operating system.
%(os)s is not currently supported by CMU Graphics. We support Python 3.%(min_minor_version)d
and higher on Windows and MacOS."""
% {'os': sys.platform, 'min_minor_version': min_minor_version})
        os._exit(1)


def verify_cpu():
    # platform.machine() describes the Python interpreter, not the hardware:
    # x64 Python running under emulation on an ARM computer reports AMD64,
    # which is supported. Only ARM64 Python reports ARM64.
    if sys.platform == "win32" and platform.machine() == "ARM64":
        print("""\
It looks like your computer uses an ARM CPU. Windows ARM is not currently
supported by CMU Graphics. Please install Python for Windows x64 instead.
This will make your computer pretend to be using an x64 CPU, which is
supported.""")
        os._exit(1)


def verify_support(zip_distribution):
    python_major, python_minor, _ = platform.python_version_tuple()
    # The zip distribution only ships native extensions for Windows and MacOS.
    if zip_distribution:
        verify_os()

    verify_cpu()

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
