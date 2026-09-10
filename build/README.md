# Build Scripts

* To update bundled pygame, run `python3 ../../../build/helpers/build_pygame_modules.py` from `cmu_graphics/libs/pygame_loader`. Then run `python3 helpers/replace_images.py` from `build` to replace the Pygame logo with the CMU Graphics icon.

## cmu_graphics_helpers

The bundled cmu_graphics_helpers binaries are built by
  `.github/workflows/buildwheels.yml`.

On any branch other than `main`, that
  workflow copies the wheels it built into
  `cmu_graphics/libs/cmu_graphics_helpers_loader/modules/` and commits them back
  to the branch, so a branch gets a zip distribution built from its own code.

To vendor wheels by hand instead — a local `maturin build`, or wheels
  downloaded from the workflow run or from PyPI — run
  `python3 build/helpers/build_cmuhelp_modules.py --wheels <dir>` from anywhere.
  It defaults to `cmu_graphics_helpers/target/wheels`, the local maturin output.
  Wheels for platforms the zip distribution doesn't ship (Linux) and sdists in
  that directory are ignored.


## MacOS code signing
Sign and notarize binaries with `notarize.py`. **The macOS binaries the
  workflow commits are not signed or notarized.** `tests/check_binaries.py`
  checks the code signature of every bundled `.so`/`.dylib` on macOS, so the
  macOS test job will fail until they are signed. Run `notarize.py` on them
  before cutting a release, or restore the previously signed macOS binaries if
  you only meant to update the Windows one.


These scripts use a variety of passwords, certificates, and keys. For notarization and deployment, use the following environment variables

```
export APPLE_ID= # your apple developer id, for notarization
export APPLE_PASSWORD= # your apple developer id password
```

For signing binaries, you'll need an Apple Developer Certificate in your keychain with the appropriate permissions.
