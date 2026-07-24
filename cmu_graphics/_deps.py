# Resolves the native dependencies for the package modules, 
# based on which distribution we are (see _dist.py).
#
# Import these from here rather than importing cairo/pygame directly, so the
# vendored-vs-pip choice lives in exactly one place:
#
#     from cmu_graphics._deps import cairo, pygame, cmu_graphics_helpers
#
# Note: modal.py can't use this shim -- it runs as a standalone subprocess
# whose sys.path is the package directory itself, so it imports libs.* flatly
# and carries its own copy of this switch.

from cmu_graphics._dist import VENDORED

if VENDORED:
    from cmu_graphics.libs import cairo_loader as cairo
    from cmu_graphics.libs import pygame_loader as pygame
    from cmu_graphics.libs import cmu_graphics_helpers_loader as cmu_graphics_helpers
else:
    import cairo
    import pygame
    import cmu_graphics_helpers
