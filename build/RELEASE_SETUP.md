# Release setup

One-time setup for the `release` job in `.github/workflows/release.yml`, which
replaces the CodeBuild deploy, and for signing in
`.github/workflows/buildwheels.yml`. Do sections 1–4 in any order, then rehearse
with a pre-release (5), release for real (6), and retire CodeBuild (7).

Values used throughout:

| | |
|---|---|
| GitHub repository | `cmu-cs-academy/desktop-cmu-graphics` |
| Workflow files | `release.yml`, `buildwheels.yml` |
| GitHub environments | `release`, `macos-signing` |
| PyPI project | `cmu-graphics` |
| S3 destination | `s3://cmu-cs-academy.lib.prod/desktop-cmu-graphics/` |
| Apple team ID | `LXH25PRRZ2` (hard-coded in `build/notarize.py`) |


## 1. GitHub `release` environment

The release job waits for approval here, and only this environment gets AWS
access.

1. Go to the repository's **Settings → Environments → New environment** and
   name it `release`.
2. Under **Deployment protection rules**, check **Required reviewers** and add
   whoever may approve releases.
3. Under **Deployment branches and tags**, choose **Selected branches and
   tags**, then **Add deployment branch or tag rule**: type **Tag**, pattern
   `v*`. Releases only run from tags, so nothing else needs access.

The variables in section 4 go in this environment, not in the
repository-wide settings.


## 2. PyPI trusted publishers

The release job publishes `cmu-graphics` and `cmu-graphics-helpers` with a
short-lived OIDC token instead of an API token. Do this for each of the two
projects:

1. Sign in to pypi.org as an owner of the project, and open **Your
   projects → <project> → Manage → Publishing**.
2. Under **Add a new publisher**, choose **GitHub** and enter:
   - Owner: `cmu-cs-academy`
   - Repository name: `desktop-cmu-graphics`
   - Workflow name: `release.yml`
   - Environment name: `release`
3. Click **Add**.
4. For `cmu-graphics-helpers`, delete its old publisher, the one for
   `buildwheels.yml` and the `pypi` environment. Nothing publishes from there
   anymore.


## 3. Apple signing and notarization secrets

Whenever `buildwheels.yml` vendors new `cmu_graphics_helpers` binaries into a
branch, it signs the macOS ones with the Developer ID Application certificate
and notarizes them with Apple. The release job only checks they're signed.

### Create the `macos-signing` environment

The signing secrets go in their own environment. It has no required reviewers,
since `buildwheels.yml` runs on pushes to any branch other than `main` and
shouldn't wait for approval. That means anyone who can push a branch can run a
workflow that reads these secrets.

1. Go to the repository's **Settings → Environments → New environment** and
   name it `macos-signing`.
2. Leave **Deployment branches and tags** at **No restriction**.

### Export the certificate

1. On a Mac whose keychain has the certificate, open **Keychain Access →
   login → My Certificates**.
2. Find **Developer ID Application: Evan Mallory (LXH25PRRZ2)**. Expand it to
   check the private key is under it; the export needs both.
3. Right-click the certificate, choose **Export**, and save it as
   `developer-id.p12`, with a strong password. That password is
   `MACOS_CERTIFICATE_PASSWORD` below.

### Create an app-specific password

1. Sign in to account.apple.com with the Apple ID that belongs to team
   `LXH25PRRZ2`.
2. Go to **Sign-In and Security → App-Specific Passwords**, and generate one
   named something like `desktop-cmu-graphics notarization`. That is
   `APPLE_PASSWORD` below.

### Store the secrets

From the repository, with the `gh` CLI signed in as a repository admin (each
command prompts for the value, except the first):

```bash
base64 -i developer-id.p12 | gh secret set MACOS_CERTIFICATE_P12 --env macos-signing
gh secret set MACOS_CERTIFICATE_PASSWORD --env macos-signing
gh secret set APPLE_ID --env macos-signing
gh secret set APPLE_PASSWORD --env macos-signing
```

`APPLE_ID` is the Apple ID's email address. Then delete `developer-id.p12`.

The same values can be entered by hand under **Settings → Environments →
macos-signing → Environment secrets**.


## 4. AWS role for the S3 upload

The release job assumes an IAM role with GitHub's OIDC token, so no AWS keys are
stored anywhere. Run these with credentials for the AWS account that owns
`cmu-cs-academy.lib.prod`.

### Allow GitHub's OIDC provider

Skip this if the account already has an identity provider for
`token.actions.githubusercontent.com` (check **IAM → Identity providers**).

```bash
aws iam create-open-id-connect-provider \
  --url https://token.actions.githubusercontent.com \
  --client-id-list sts.amazonaws.com
```

### Create the role

Save this as `trust.json`, with the account ID filled in. It lets only jobs
in this repository's `release` environment assume the role.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
          "token.actions.githubusercontent.com:sub": "repo:cmu-cs-academy/desktop-cmu-graphics:environment:release"
        }
      }
    }
  ]
}
```

Save this as `upload.json`. It allows writing into the zip distribution's
prefix, and nothing else.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::cmu-cs-academy.lib.prod/desktop-cmu-graphics/*"
    }
  ]
}
```

Then:

```bash
aws iam create-role --role-name desktop-cmu-graphics-release \
  --assume-role-policy-document file://trust.json
aws iam put-role-policy --role-name desktop-cmu-graphics-release \
  --policy-name upload-zip-distribution --policy-document file://upload.json
```

### Tell the workflow about it

```bash
gh variable set AWS_RELEASE_ROLE_ARN --env release \
  --body "arn:aws:iam::<ACCOUNT_ID>:role/desktop-cmu-graphics-release"
```

The workflow assumes the bucket is in `us-east-1`. Check with
`aws s3api get-bucket-location --bucket cmu-cs-academy.lib.prod`; a
`LocationConstraint` of `null` means `us-east-1`. For any other region, also
run `gh variable set AWS_REGION --env release --body <region>`.


## 5. Rehearse with a pre-release

A pre-release tag runs the whole release job except the S3 upload: it checks
the zip's signatures and publishes to PyPI, where pip ignores pre-releases unless asked.

1. Set `cmu_graphics/meta/version.txt` to `3.0.1rc1`, and merge that to `main`.
2. Tag it: `git tag v3.0.1rc1 && git push origin v3.0.1rc1`.
3. In the Release run for the tag, approve the `release` job.
4. Check that:
   - pypi.org lists `cmu-graphics 3.0.1rc1`, and
     `pip install --pre cmu-graphics==3.0.1rc1` works on macOS, Windows, and
     Linux.
   - The run's `zip-distribution` artifact, downloaded with a browser (so macOS
     quarantines it, as it would for a student), unzips and runs a sample
     without a Gatekeeper warning on a Mac, and runs on Windows.
   - `version.txt` on S3 is unchanged.

If a step after publishing fails, re-running the job is safe: the publish step
skips files PyPI already has.


## 6. Release

1. Set `cmu_graphics/meta/version.txt` to `3.0.1`, and merge that to `main`.
2. `git tag v3.0.1 && git push origin v3.0.1`, and approve the `release` job.
3. Check that the upload landed:
   `curl https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/version.txt`
   prints `3.0.1`.


## 7. Retire CodeBuild

Once 3.0.1 is out:

1. In the AWS console, open **CodeBuild**, find the project that runs
   `buildspec-deploy.yml`, and delete it (or remove its trigger, if you want
   to keep its history for a while). The buildspec is already gone from the
   repository, so a leftover trigger would only produce failing builds.
2. On pypi.org, under **Account settings → API tokens**, delete the tokens
   CodeBuild used (its `PYPI_TOKEN` and `PYPI_TEST_TOKEN`), and remove them
   from wherever the CodeBuild project read them, such as its environment
   variables or Secrets Manager.
3. Remove the CodeBuild project's IAM role or S3 permissions if nothing else
   uses them.
4. Delete the repository's `pypi` and `testpypi` environments (**Settings →
   Environments**). No workflow uses them anymore.
