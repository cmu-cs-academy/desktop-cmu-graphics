# Which distribution of CMU Graphics this source targets.
#
# Checked in as VENDORED = True, which is what BOTH the desktop zip installer
# and local development use: they always load the vendored cairo/pygame
# binaries shipped under cmu_graphics/libs, never whatever might be installed
# on the system (student machines often have broken system installs).
#
# The PyPI build step rewrites this to False before building the wheel, where
# cairo/pygame come from pip instead. This constant is the single, static
# source of truth for that difference.

VENDORED = True
