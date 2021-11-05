# Build Scripts

This folder contains scripts for

* Building binaries `binaries.sh`
* Run `python3 ../../../build/helpers/build_pygame_modules.py` from `cmu_graphics/libs/pygame_loader`
* Manually download Pillow wheels for any new platforms, and copy the PIL folder out of them to cmu_graphics/libs/pil_loader
* Setting up modules `modules.sh`
* Signing and notarizing binaries `notarize.sh`

These scripts use a variety of passwords, certificates, and keys. For notarization and deployment, use the following environment variables

```
export APPLE_ID= # your apple developer id, for notarization
export APPLE_PASSWORD= # your apple developer id password
export AWS_ACCESS_KEY_ID= # an access key for your AWS S3 bucket
export AWS_SECRET_ACCESS_KEY= # a secret key for the above access key
```

For signing binaries, you'll need an Apple Developer Certificate in your keychain with the appropriate permissions.
