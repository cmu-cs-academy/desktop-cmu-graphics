# Getting started

1. [Have a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
2. Download the following programs:

    - GIT: https://git-scm.com/downloads
    - Python: https://www.python.org/downloads/
    - An IDE (we recommend VSCode)
    - If you running on a Mac, install pkg-config with [homebrew](https://brew.sh/): `brew install pkg-config`

3. [Fork the repo to your own GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)
4. [Clone your fork to your local machine](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)

# Project Structure

Inside of `desktop-cmu-graphics` you will find the following...

- `build/` Various scripts related to building the downloadable zip file.
- `documentation/` Some documentation related to development.
- `samples/` Some sample code that uses `cmu_graphics`.
- `tests/` Test cases for testing the library and making sure that code changes don't break things.
- `cmu_graphics` The actual code for the graphics library itself.

    - `cmu_graphics.py` The main library code
    - `shape_logic.py` The shapes (or shape like things) that can be drawn
    - `utils.py` The various utility functions provided for users
    - `sound.py` The code to handle sound
    - `modal.py` Code for app.getTextInput and app.showMessage

# Preparing the Local Workspace

There are a number of dependencies that need to be installed:

```
cd <path/to/desktop-cmu-graphics>
uv run pre-commit install --install-hooks
```

If you're working on the Rust helpers library, install Rust via rustup as described [here](https://rust-lang.org/tools/install/). See the section about configuration your `PATH` environment
variable to ensure `cargo` and `rustc` are both available.


# Running a Build

To build the installer zip file, run...

```
uv run build/build.py
```

# Testing

Before creating a new pull request, you should run the test suite to make sure your changes haven't broken anything.

## Setup for Testing

- Build the library as described above in "Running a Build"

## Running the test cases

Run tox:

```
uv run tox
```

This will run the tests using a bunch of different versions of python. The tests will fail for particular "environments" if you don't have the necessary version of python already installed. After running tox once for all environments, you can run it for just a single environment so that it is much faster. Pick an environment that succeeded the first time, e.g. `py314-pip` and pass that to tox:

```
uv run tox -e py314-pip
```

## Using the test output

If tox gives an error, it can be helpful to run the specific test that failed without using tox. Tests are located in:

- `tests/test_get_text_input.py`
- `tests/test_sound.py`
- `tests/test_image_gen.py`

To run a test in isolation, run (change py314-pip to the name of the tox environment you want to use)...

    cd /path/to/desktop-cmu-graphics/.tox/py314-pip/tmp
    source ../bin/activate
    rm -rf image_gen
    python /path/to/desktop-cmu-graphics/tests/<test_name.py>

## Image Generation Tests

`test_image_gen.py` runs a variety of test cases that produce images.  If it fails, it will produce a `report.html` file that contains info on the sub-tests that failed.

The report will have 3 images on top (correct image, output image and difference image respectively) as well as the entire test code. Copy that test code in a new python file and run it to reproduce the error.

Prior to re-running `test_image_gen.py`, delete the generated folder `image_gen`.

Test apps run in hidden windows, which are never shown and never take focus, so you can keep using your computer while the tests run. `tox.ini` and `test_image_gen.py` do this by setting the `CMU_GRAPHICS_HIDDEN_WINDOW` environment variable. To watch a failing test run, pass `--show-windows`:

    python /path/to/desktop-cmu-graphics/tests/test_image_gen.py --show-windows --only <test_name.py>

On a HiDPI screen (such as a Retina Mac), screenshots are taken at the screen's scale and scaled down to the app's size before comparison. Tests that draw images get a looser threshold there, since images are sampled from their source at a higher resolution.

### Event tests

Tests named `image_gen/events_*.py` run like a normal app that calls `runApp()` itself. They drive the app with injected mouse and resize events (`injectMouseMove`, `injectMousePress`, `injectMouseRelease`, `injectResize`), which go through the event loop's real handling of OS input, and call `screenshotAndQuit()` once they're done. Draw only axis-aligned rectangles at whole-pixel positions in these tests, so their correct images match on every screen scale.

`test_image_gen.py` also runs behavior tests that check timing (step rate and idle redraws) and print `PASS`/`FAIL` lines instead of producing an image.

To add a correct image for a new test, run it once; the missing `correct_1.png` is generated in the working copy of `image_gen`. Check that it looks right, then copy it into `tests/image_gen/<test name>/`.

### Manual testing

Some behavior can't be tested automatically, because keyboard input can't be injected and the text input modal runs in its own process. When changing event handling, check these by hand on macOS, Windows, and Linux:

- Holding a key down calls `onKeyPress` once, then `onKeyHold` each step, until it's released.
- In the `app.getTextInput()` modal, dragging across typed text selects it, and the selection follows the mouse, including past either end of the box.
- Holding backspace in the modal deletes one character, then repeats at a steady rate after a short delay.

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

# Translation

Translation into Spanish and German is handled by a library.
You don't need to edit the content between `# start_translate` and `# end_translate`.
