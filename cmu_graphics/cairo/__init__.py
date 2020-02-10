import os

def get_valid_cairo_module():
    current_directory = os.path.dirname(__file__)
    modules = os.path.join(current_directory, 'modules')
    for module in os.listdir(modules):
        if module.startswith('cairo_'):
            try:
                cairo = __import__(module)
                return cairo
            except ModuleNotFoundError:
                continue
    return None

cairo = get_valid_cairo_module()
if cairo is None:
    error_string = (
        "We do not have a precompiled version of cairo available "
        + "for your operating system and computer. You may need to install "
        + "cairo manually."
    )
    raise Exception(error_string)

from cairo import *
