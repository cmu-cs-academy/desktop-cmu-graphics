import os
import sys
from .. import loader_util

current_directory = os.path.dirname(__file__)
module_directory = os.path.join(current_directory, 'modules')
module_path = os.path.join(module_directory, 'pil_' + loader_util.get_platform_string())
sys.path.append(module_path)

from PIL import Image

globals().update(Image.__dict__)
