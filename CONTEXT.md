# Desktop CMU Graphics

The desktop version of the graphics framework used by CMU CS Academy, shipped to beginner students outside the browser.

## Language

### Distributions

**Zip distribution**:
The archive students download from academy.cs.cmu.edu/desktop and unzip next to their own code. It must work without installing anything, so it carries its own copy of the native extension.
_Avoid_: installer, vendored build, zip installer

**Pip distribution**:
The `cmu-graphics` package installed from PyPI with `pip install cmu-graphics`.
_Avoid_: pypi package, wheel (when meaning the distribution as a whole)

**Native extension**:
The compiled Rust module that `cmu_graphics` uses for drawing, windowing, sound, and geometry. It is part of `cmu-graphics`, not a separately published package.
_Avoid_: helpers, helpers package, cmu_graphics_helpers, vendored binaries
