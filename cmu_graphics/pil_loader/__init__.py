import os
import sys
import importlib

try:
    importError = ModuleNotFoundError
except NameError:
    importError = ImportError

def get_valid_pil_module():
    current_directory = os.path.dirname(__file__)
    modules = os.path.join(current_directory, 'modules')
    for module in os.listdir(modules):
        if module.startswith('pil_'):
            try:
                module_path = '%s%smodules%s%s' % (current_directory, os.sep, os.sep, module)
                sys.path.append(module_path)
                pil = importlib.import_module('PIL')
                return pil
            except importError as e:
                print(e)
                print(sys.path.pop())
    return None

PIL = get_valid_pil_module()
if PIL is None:
    error_string = (
        "We do not have a precompiled version of pil available "
        + "for your operating system and computer. You may need to install "
        + "pil manually."
    )
    raise Exception(error_string)

globals().update(PIL.__dict__)
