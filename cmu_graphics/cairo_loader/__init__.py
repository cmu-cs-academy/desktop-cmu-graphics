import os
import sys
import importlib

try:
    importError = ModuleNotFoundError
except NameError:
    importError = ImportError

def get_valid_cairo_module():
    current_directory = os.path.dirname(__file__)
    modules = os.path.join(current_directory, 'modules')
    for module in os.listdir(modules):
        if module.startswith('cairo_'):
            try:
                module_path = '%s%smodules%s%s' % (current_directory, os.sep, os.sep, module)
                sys.path.append(module_path)
                cairo = importlib.import_module('cairo')
                return cairo
            except importError:
                sys.path.pop()
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
