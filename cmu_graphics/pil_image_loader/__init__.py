import os
import sys
import importlib

try:
    ModuleNotFoundError
except NameError:
    ModuleNotFoundError = ImportError

def get_valid_pil_image_module():
    current_directory = os.path.dirname(__file__)
    modules = os.path.join(current_directory, 'modules')
    for module in os.listdir(modules):
        if module.startswith('pil_'):
            try:
                module_path = '%s%smodules%s%s' % (current_directory, os.sep, os.sep, module)
                sys.path.append(module_path)
                if 'PIL' in sys.modules:
                    del sys.modules['PIL']
                from PIL import Image
                return Image
            except (ModuleNotFoundError, ImportError) as e:
                sys.path.pop()

PIL_Image = get_valid_pil_image_module()
if PIL_Image is None:
    error_string = (
        "We do not have a precompiled version of pygame available "
        + "for your operating system and computer. You may need to install "
        + "pygame manually."
    )
    raise Exception(error_string)

globals().update(PIL_Image.__dict__)
