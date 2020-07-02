# Build Scripts

This folder contains scripts for

* Building binaries `binaries.sh`
* Setting up modules `modules.sh`
* Creating and signing a release zip `release.sh`

`binaries.sh` and `release.sh` both upload to our AWS S3 bucket. Run `aws configure` to set up your credentials before running these.

To run `release.sh` you will also need an Apple Develop ID Certificate in your Mac Keychain (for signing) and environment variables `APPLE_ID` and `APPLE_PASSWORD` (for notarization).
