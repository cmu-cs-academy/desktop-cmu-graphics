# The native extension, cmu_graphics._native, which is built from the Rust
# crate in native/. Both distributions ship it inside the cmu_graphics package:
# the zip distribution holds one copy per platform side by side, and Python
# picks the one for this platform by its file extension.
#
# Import it from here rather than directly:
#
#     from cmu_graphics.deps import wyvern, pygeo
#
# This module gets imported two ways. Usually it is `cmu_graphics.deps`. But
# modal.py runs as a standalone subprocess whose sys.path[0] is the package
# directory itself -- there the name `cmu_graphics` resolves to the sibling
# cmu_graphics.py module rather than to the package, so modal.py has to import
# this flatly, as `deps`, and the native extension is then `_native`.

__all__ = ['__version__', 'pygeo', 'wyvern']

if __package__:
    from . import _native
else:
    import _native

__version__ = _native.__version__
wyvern = _native.wyvern
pygeo = _native.pygeo
