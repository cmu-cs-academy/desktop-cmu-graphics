# Windows

We've been able to reliably find compiled Windows binaries for cairo here:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo

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
python3 -m pip install --upgrade setuptools wheel delocate
```

Run these lines from the "build" directory. This downlods the pycairo source and moves to the commit we've picked for consistency.

```
git clone https://github.com/pygobject/pycairo.git
cd pycairo
export PYCAIRO_COMMIT=27c0d7c074f52aabd28ec652a6727ffeacb81125
git checkout $PYCAIRO_COMMIT
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
pkg config needs to know how to access libffi and cairo. These are the paths
that brew uses to install those libraries for me:

```
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig:/usr/local/opt/cairo/lib/pkgconfig/"
```

Compile the wheel:

```
python3 setup.py sdist bdist_wheel
```

setup.py may be claiming to be building a universal2 wheel even if you've specified
a particular architecture. That seems to be a lie, so it's ok to disregard.

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

You'll need to pick an appropriate path to put the delocated binaries in.
Our convention is to use e.g. "cpython-311-darwin_dylibs" 
for a file named "_cairo.cpython-311-darwin.so". Take the middle of the
binary name (after _cairo. and before .so) and add "_dylibs" to the end.

The following command should be run from `dist`. You want to delocate
the "cairo" directory, which contains the file like 
"_cairo.cpython-311-darwin.so". This should produce a folder like
"cpython-311-darwin_dylibs" in "dist/cairo" which has many .dylib files.

```
export libpath="cpython-311-darwin_dylibs"
delocate-path --lib-path=$libpath cairo
```

Once you've done this, you can move the .so file and the dylibs directory
to the appropriate spots in `cmu_graphics/libs`.