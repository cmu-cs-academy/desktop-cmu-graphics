# Getting started

1. [Have a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
2. Download the following programs on your os:

    - GIT: https://git-scm.com/downloads
    - Python: https://www.python.org/downloads/
    - An IDE (we recommend PyCharm or VSCode)
    - You may also find yourself prompted to install cmake and-or zlib at some point, but if not don't worry about it.
3. [Fork the repo to your own GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)
4. [Clone your fork to your local machine](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)

# Project Structure

Inside of `desktop-cmu-graphics` you will find the following...

- `build/` Various scripts related to building the downloadable zip file.
- `documentation/` Some documentation related to development.  (Currently very sparse.)
- `samples/` Some sample code that uses `cmu_graphics`.
- `tests/` Testcases for testing the library and making sure that code changes don't break things.
- `cmu_graphics` The actual code for the graphics library itself.

    - `cmu_graphics.py` The main library code
    - `shape_logic.py` The shapes (or shape like things) that can be drawn
    - `utils.py` The various utility functions provided for users
    - `sound.py` The code to handle sound
    - `modal.py` **!!I have no idea, someone else should update this!!**

# Preparing the Local Workspace

1. There are a number of dependencies that need to be installed:

        cd <path/to/desktop-cmu-graphics>
        python -m venv venv
        source venv/Scripts/activate (if on Windows)
        source venv/bin/activate     (otherwise)
        pip install twine build tox

2. Install `cmu_graphics` into the local virtual environment as editable:  

        pip install -e .

    (If this fails, modify `desktop-cmu-graphics/setup.py` on line 33 and remove cmu_graphics.samples`)


# Running a Build

To build the installer zip file, do...

```
python build/build.py
```

# Testing

Before building, it might be useful to run the testsuite to make sure your changes haven't broken anything.

## Setup for Testing

- Build the pip and zip packages:

      python build/build.py

- Install testing dependencies:

      pip install psutil pillow imageio numpy

## Running the Testcases

Run tox:

```
tox
```

After the first time of running tox successfully, we recommend you changing your `tox.ini` file to only run the tests once, by restricting the interpreters to one that worked the first time.

For example, the second line should go from something like this:  
`envlist=py{38,39,310,311,312}-{pip,zip}`  
To something like this:  
`envlist=py{311}-{pip}`

## Using the test output

If tox gives an error, try running the specific test that failed.  Tests are located in:  
- `tests/test_get_text_input.py`
- `tests/test_sound.py`
- `tests/test_image_gen.py`

To run a test in isolation, do...

    python tests/<test_name>

## Image Generation Tests

`test_image_gen.py` runs a variety of testcases that produce images.  If it fails, it will produce a `report.html` file that contains info on the sub-tests that failed.

The report will have 3 images on top (correct image, output image and difference image respectively) as well as the entire test code. Copy that test code in a new python file and run it to get to the place that threw the error. From there happy debugging.

Prior to re-running `test_image_gen.py`, delete the generated folder `image_gen`.

# Submitting Changes

Once you have fixed a bug or added a new features, the next step is to submit your changes back to the project so that others can benefit.

1. Create a new branch in your fork with a simple descriptive name (e.g., `new_feature_\<feature name>`).
2. Implement your changes locally on the branch. Use multiple short and descriptive commits. And test your code!
3. Push commits to GitHub using VSCode UI or `git push`.
4. Create pull request
    - [Open a PR on GitHub.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
    - Include details like what's changed and why.
5. We'll review your PR and provide feedback if needed. Changes might be requested.
6. If your pull request is approved, it will be merged.  Thanks for your contribution!