### ZIPFILE VERSION ###
import sys
import struct
### END ZIPFILE VERSION ###
import platform
import os

min_minor_version = 9
max_minor_version = 13

### ZIPFILE VERSION ###
def get_platform_string():
    plat = "unsupported"
    if sys.platform == "darwin":
        plat = "mac"
        if platform.machine() == 'arm64':
            plat += '_arm'
    elif sys.platform == "win32":
        plat = "win"
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
through Python 3.%(max_minor_version)d on Windows and MacOS.""" 
% {'os': sys.platform, 'max_minor_version': max_minor_version, 'min_minor_version': min_minor_version})
        os._exit(1)
        
### END ZIPFILE VERSION ###

def verify_support():
    python_major, python_minor, _ = platform.python_version_tuple()
    ### ZIPFILE VERSION ###
    verify_os()
    ### END ZIPFILE VERSION ###

    if python_major != '3':
        print("""\
It looks like you're running a version of Python 2. Since Python 2 is no
longer maintaned as of January 1 2020, CMU Graphics does not support Python 2.
We recommend installing Python 3.%(max_minor_version)d from python.org"""
% {'max_minor_version': max_minor_version})
        os._exit(1)

    ### ZIPFILE VERSION ###
    if int(python_minor) > max_minor_version:
        print("""\
It looks like you're running Python 3.%(minor)s. Python 3.%(minor)s is not currently
supported by CMU Graphics. We support Python 3.%(min_minor_version)d-3.%(max_minor_version)d. We recommend
installing Python 3.%(max_minor_version)d from python.org""" %
{"minor": python_minor, 'max_minor_version': max_minor_version, 'min_minor_version': min_minor_version})
        os._exit(1)
    ### END ZIPFILE VERSION ###

    if int(python_minor) < min_minor_version:
        print("""\
It looks like you're running Python 3.%(minor)s. Python 3.%(minor)s is not currently
supported by CMU Graphics. We support Python 3.%(min_minor_version)d and higher. We recommend 
installing Python 3.%(max_minor_version)d from python.org""" %
{"minor": python_minor, 'max_minor_version': max_minor_version, 'min_minor_version': min_minor_version})
        os._exit(1)
