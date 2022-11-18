import os
import sys
from .. import loader_util

current_directory = os.path.dirname(__file__)
module_directory = os.path.join(current_directory, 'modules')
module_path = os.path.join(module_directory, 'pygame_' + loader_util.get_platform_string())
sys.path.append(module_path)

import pygame

globals().update(pygame.__dict__)
