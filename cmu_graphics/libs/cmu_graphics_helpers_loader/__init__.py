import os
import sys
from .. import loader_util

current_directory = os.path.dirname(__file__)
module_directory = os.path.join(current_directory, 'modules')
module_path = os.path.join(module_directory, 'cmu_graphics_helpers_' + loader_util.get_platform_string())
sys.path.insert(0, module_path)

import cmu_graphics_helpers

globals().update(cmu_graphics_helpers.__dict__)
