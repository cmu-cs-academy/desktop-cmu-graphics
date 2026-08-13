# Resolves the native dependencies for the package modules,
# based on which distribution we are (see dist.py).
#
# Import these from here rather than importing pygame/cmu_graphics_helpers
# directly, so the vendored-vs-pip choice lives in exactly one place:
#
#     from cmu_graphics.deps import pygame, cmu_graphics_helpers
#
# This module gets imported two ways. Usually it is `cmu_graphics.deps`. But
# modal.py runs as a standalone subprocess whose sys.path[0] is the package
# directory itself -- there the name `cmu_graphics` resolves to the sibling
# cmu_graphics.py module rather than to the package, so modal.py has to import
# this flatly, as `deps`. Deriving the prefix from __package__ ('cmu_graphics'
# in the first case, '' in the second) makes the same code work for both.

import importlib

_prefix = __package__ + '.' if __package__ else ''

VENDORED = importlib.import_module(_prefix + 'dist').VENDORED

if VENDORED:
    pygame = importlib.import_module(_prefix + 'libs.pygame_loader')
    cmu_graphics_helpers = importlib.import_module(
        _prefix + 'libs.cmu_graphics_helpers_loader'
    )
    wyvern = cmu_graphics_helpers.wyvern
    pygeo = cmu_graphics_helpers.pygeo
else:
    import pygame
    import cmu_graphics_helpers
