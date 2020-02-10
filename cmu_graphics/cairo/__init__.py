import os
import sys
import importlib

def get_valid_cairo_module():
    current_directory = os.path.dirname(__file__)
    modules = os.path.join(current_directory, 'modules')
    sys.path.append(current_directory)
    for module in os.listdir(modules):
        if module.startswith('cairo_'):
            try:
                cairo = importlib.import_module(f'modules.{module}')
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

globals().update(cairo.__dict__)
