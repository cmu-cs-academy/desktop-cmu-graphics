# Build Scripts

This folder contains scripts for

* To update bundled pygame, run `python3 ../../../build/helpers/build_pygame_modules.py` from `cmu_graphics/libs/pygame_loader`. Then run `replace_images.py` to replace the Pygame logo with the CMU Graphics icon.
* To update bundled pillow, manually download pillow wheels for any new platforms, and copy the PIL folder out of them to cmu_graphics/libs/pil_loader
* To update bundled cairo, follow the instructions in build_cairo_binaries.md
* Sign and notarize binaries with `notarize.sh`

These scripts use a variety of passwords, certificates, and keys. For notarization and deployment, use the following environment variables

```
export APPLE_ID= # your apple developer id, for notarization
export APPLE_PASSWORD= # your apple developer id password
export AWS_ACCESS_KEY_ID= # an access key for your AWS S3 bucket
export AWS_SECRET_ACCESS_KEY= # a secret key for the above access key
```

For signing binaries, you'll need an Apple Developer Certificate in your keychain with the appropriate permissions.
