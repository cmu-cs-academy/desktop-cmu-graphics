# Which distribution of CMU Graphics this source targets.
#
# Checked in as VENDORED = False, which is what local development and the PyPI
# package use: cmu_graphics_helpers is imported as an installed package. In a
# checkout of this repository, `uv sync` (or `uv run`) builds it from
# cmu_graphics_helpers/ into the virtual environment, so changes to the Rust
# source take effect without vendoring new binaries.
#
# build/build.py rewrites this to True in the desktop zip installer's copy,
# which loads the vendored cmu_graphics_helpers binaries shipped under
# cmu_graphics/libs, never whatever might be installed on the system (student
# machines often have broken system installs). This constant is the single,
# static source of truth for that difference.

VENDORED = False
