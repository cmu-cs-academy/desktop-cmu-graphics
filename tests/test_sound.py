import os

CMU_GRAPHICS_DEBUG = True
from cmu_graphics import *

os.environ["SDL_AUDIODRIVER"] = "dummy"

music = Sound('https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/Liberty_bell_march.mp3')
os._exit(0)
