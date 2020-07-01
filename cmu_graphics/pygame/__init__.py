import os
import sys
import importlib

def get_valid_pygame_module():
    current_directory = os.path.dirname(__file__)
    modules = os.path.join(current_directory, 'modules')
    for module in os.listdir(modules):
        if module.startswith('pygame_'):
            try:
                module_path = f'{current_directory}{os.sep}modules{os.sep}{module}'
                sys.path.append(module_path)
                pygame = importlib.import_module('pygame')
                return pygame
            except ModuleNotFoundError:
                sys.path.pop()
    return None

pygame = get_valid_pygame_module()
if pygame is None:
    error_string = (
        "We do not have a precompiled version of pygame available "
        + "for your operating system and computer. You may need to install "
        + "pygame manually."
    )
    raise Exception(error_string)

globals().update(pygame.__dict__)
