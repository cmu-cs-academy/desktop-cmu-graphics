# Build Scripts

* To update bundled pygame, run `python3 ../../../build/helpers/build_pygame_modules.py` from `cmu_graphics/libs/pygame_loader`. Then run `python3 helpers/replace_images.py` from `build` to replace the Pygame logo with the CMU Graphics icon.
* To update bundled cairo, follow the instructions in build_cairo_binaries.md
* Sign and notarize binaries with `notarize.py`

These scripts use a variety of passwords, certificates, and keys. For notarization and deployment, use the following environment variables

```
export APPLE_ID= # your apple developer id, for notarization
export APPLE_PASSWORD= # your apple developer id password
```

For signing binaries, you'll need an Apple Developer Certificate in your keychain with the appropriate permissions.
