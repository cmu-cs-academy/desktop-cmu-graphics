# Build Scripts

This folder contains scripts for

* Building binaries `binaries.sh`
* Setting up modules `modules.sh`
* Creating and signing a release zip `release.sh`

`./release.sh --deploy` uploads to the S3 bucket

These scripts use a variety of passwords, certificates, and keys, all of which should be stored in the following environment variables

```
export APPLE_ID= # your apple developer id, for notarization
export APPLE_PASSWORD= # your apple developer id password
export AWS_ACCESS_KEY_ID= # an access key for your AWS S3 bucket
export AWS_SECRET_ACCESS_KEY= # a secret key for the above access key
export SIGNING_IDENTITY_P12_B64= # a base64 encoded version of your private.p12 file from Apple, for signing binaries
export SIGNING_IDENTITY_PASSWORD= # the password to unlock your private.p12 file
```
