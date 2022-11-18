
import platform
import os



def verify_support():
    python_major, python_minor, _ = platform.python_version_tuple()
    

    if python_major != '3':
        print("""\
It looks like you're running a version of Python 2. Since Python 2 is no
longer maintaned as of January 1 2020, CMU Graphics does not support Python 2.
We recommend installing Python 3.10 from python.org""")
        os._exit(1)

    

    if int(python_minor) < 6:
        print("""\
It looks like you're running Python 3.%(minor)s. Python 3.%(minor)s is not currently
supported by CMU Graphics. We support Python 3.6 and higher. We recommend 
installing Python 3.10 from python.org""" %
{"minor": python_minor})
        os._exit(1)
