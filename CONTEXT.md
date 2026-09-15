# CMU Graphics desktop

The desktop (non-web) distribution of CMU CS Academy's graphics framework, for students running their programs locally.

## Language

### Distributions

**Vendored distribution**:
The installer zip, which bundles cmu_graphics with prebuilt pygame and helpers binaries. Supports Mac and Windows only.
_Avoid_: zip installer, desktop installer

**Pip distribution**:
The `cmu-graphics` package on PyPI, which gets pygame-ce and the helpers as dependencies. Supports Mac, Windows, and Linux.
_Avoid_: PyPI package, pip install

**Helpers**:
`cmu_graphics_helpers`, the Rust extension (built on Skia) that draws shapes and text; its drawing API is the `wyvern` module. Published to PyPI as `cmu-graphics-helpers` and bundled into the vendored distribution.
_Avoid_: the Rust module

### Tests

**Baseline**:
The checked-in image (`correct_N.png`) that an image test's screenshot is compared against.
_Avoid_: golden image, expected image

**Linux baseline**:
A `linux_correct_N.png` that replaces a test's baseline when running on Linux, where text renders with different fonts.
_Avoid_: platform baseline
