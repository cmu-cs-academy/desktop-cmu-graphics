import os
import sys
import importlib

def get_valid_pygame_module():
    current_directory = os.path.dirname(__file__)
    modules = os.path.join(current_directory, 'modules')
    sys.path.append(current_directory)
    for module in os.listdir(modules):
        if module.startswith('pygame_'):
            try:
                pygame = importlib.import_module(f'modules.{module}')
                return pygame
            except ModuleNotFoundError:
                continue
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
