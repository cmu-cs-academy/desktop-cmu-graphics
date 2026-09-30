# Which distribution of CMU Graphics this source is part of.
#
# Checked in as ZIP_DISTRIBUTION = False, which is what local development and
# the pip distribution use.
#
# build/build.py rewrites this to True in the zip distribution's copy. The zip
# distribution only supports Windows and macOS, and tells students to upgrade
# by downloading it again rather than with pip. This constant is the single,
# static source of truth for that difference.

ZIP_DISTRIBUTION = False
