# Build the Linux helpers wheel on manylinux_2_34

The Linux cmu_graphics_helpers wheel bundles the FreeType from its manylinux build container, and Skia needs FreeType 2.10+ (`FT_Palette_Data_Get`). The manylinux2014 container ships FreeType 2.8, so wheels built there fail to import on every Linux system. We build on manylinux_2_34 (FreeType 2.10.4), which keeps Skia's prebuilt binaries and a self-contained wheel, at the cost of requiring glibc 2.34+ (Ubuntu 22.04+, Debian 12+, Fedora 35+). Older distros can't install the wheel.

## Considered Options

- **skia-safe's `embed-freetype` feature**: works on any glibc, but rust-skia publishes no prebuilt Linux binaries with it, so Skia would be compiled from source in CI (roughly 30+ extra minutes per build), and the wheel would still bundle manylinux2014's old fontconfig.
- **Excluding FreeType from the wheel** (stay on manylinux2014 and link the system's FreeType): the wheel would break on any system with FreeType older than 2.10, and a manylinux wheel is expected to bundle its non-system libraries.
