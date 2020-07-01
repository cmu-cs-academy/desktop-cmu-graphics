# Build Scripts

This folder contains scripts for

* Building binaries `binaries.sh`
* Setting up modules `modules.sh`
* Creating and signing a release zip `release.sh`

These scripts use a variety of environment variables which should be exported from an untracked file `env.sh`.

`env.sh` should include the following variables and look like this

```
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_BUCKET=s3://

export PYCAIRO_COMMIT=
```
