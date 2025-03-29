# Windows

The PyPi wheels for Windows can be vendored directly, just like the Pygame
and PIL wheels.

Wheels downloaded from PyPi will not include a cairo.dll file like the old
gholke binaries did, but they work anyway. Cairo seems to be bundled directly
into the extension module (we think).

# Mac:

MacOS binaries for pycairo must be compiled from scratch.
Here are some instructions for doing so:

<hr/>

You will need the following libraries/tools, which can be installed with
brew:

```
pkg-config
cairo
```

**Make sure these libraries are installed.**  If cairo is not installed, the build will appear to succeed, but pycairo will fail to import with a cryptic warning.

If you've previously installed one of these libraries and you'd like to ugrade
it, you can use `brew upgrade packagename`.

You may also need to to pip install the package "delocate" globally (outside of a virtualenv) in order to run the `delocate-path` command later on.

Deactivate any active virtual environments.

Run these lines from the "build" directory, making sure "python3" points
to the version of Python you'd like to build for. This creates a virtual environment with the right version of Python and installs the right libraries for building cairo.

```
python3 -m pip install --upgrade virtualenv
python3 -m virtualenv ../venv -p python3
source ../venv/bin/activate
python3 -m pip install --upgrade build delocate
```

Run these lines from the "build" directory. This downlods the pycairo source and moves to the commit we've picked for consistency.

```
git clone https://github.com/pygobject/pycairo.git
cd pycairo
git checkout 625613c7cf7a1bea76252fdfe97f7ca0b0d86af2
```

By default, setup.py will try to compile a universal2 binary. This is probably something good to do in the long run, but we're not set up to use universal binaries right now, and delocating those binaries may require some extra work.

So for now, we'll use some environment variables to compile for only one architecture at a time.

To compile for x86 (which must be done on an x86 machine) use

```
export ARCHFLAGS="-arch x86_64"
export LDFLAGS="-arch x86_64"
```

To compile for arm (which must be done on an arm machine) use

```
export ARCHFLAGS="-arch arm64"
export LDFLAGS="-arch arm64"
```

To compile on any architecture, we need PKG_CONFIG_PATH set up right.
pkg config needs to know how to access libffi and cairo (probably --
libffi may not actually be necessary to add here, something to look into in the
future).

These are the paths that brew uses to install those libraries for me on my x86 machine:

```
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig:/usr/local/opt/cairo/lib/pkgconfig/"
```

And on my arm machine:

```
export PKG_CONFIG_PATH="/opt/homebrew/Library/Homebrew/os/mac/pkgconfig/:/opt/homebrew/lib/pkgconfig/"
```

These lines were useful for me in finding the right paths to add to PKG_CONFIG_PATH:

```
find /opt -name cairo.pc
find /opt -name libffi.pc
```

Note that Homebrew installs into `/opt` on arm machines, and `/usr` on x86 machines.

Compile the wheel:

```
python3 -m build -w
```

The wheel is built and placed in the "dist" directory. Next, move to the dist
directory and unzip the wheel:

```
cd dist
mv *.whl wheel
unzip wheel
```

Unzipping the file produces two folders, one of which is called "cairo".
That's the one we care about. There should be one binary in there, which
we will need to delocate.

You'll need to pick an appropriate folder name for the delocated binaries.
Our convention is to use e.g. "cpython-311-darwin_dylibs"
for an .so file named "_cairo.cpython-311-darwin.so". Take the middle of the
binary name (after _cairo. and before .so) and add "_dylibs" to the end.

The following command should be run from `dist`. You want to delocate
the "cairo" directory, which contains the file like
"_cairo.cpython-311-darwin.so". This should produce a folder like
"cpython-311-darwin_dylibs" in "dist/cairo" which has many .dylib files inside.

```
delocate-path --lib-path="cpython-311-darwin_dylibs" cairo
```

Once you've done this, you can move the .so file and the dylibs directory
to the appropriate spots in `cmu_graphics/libs`.