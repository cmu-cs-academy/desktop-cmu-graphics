import os
import sys
from .. import loader_util

current_directory = os.path.dirname(os.path.realpath(__file__))
module_directory = os.path.join(current_directory, 'modules')
platform = loader_util.get_platform_string()
if 'mac' in platform:
    platform = '_'.join(platform.split('_')[:-1])
module_path = os.path.join(module_directory, 'cairo_' + platform)
sys.path.insert(0, module_path)

import cairo

globals().update(cairo.__dict__)
