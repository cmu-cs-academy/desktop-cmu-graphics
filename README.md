![Desktop CMU Graphics logo](https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/docs-media/pkg-logo.png)

Desktop CMU Graphics is an offline version of CMU Graphics, a
persistent-object graphics package geared towards beginner computer science
students. CMU Graphics and its desktop version are maintained by
[CMU CS Academy](https://academy.cs.cmu.edu/splash), a free-to-use middle and
high school computer science curriculum developed by Carnegie Mellon University.

Desktop CMU Graphics works with **Python 3.6-3.9** and is compatible with
[Replit](https://replit.com/) (see "Replit" section below). This
package, including its documentation, is licensed under the
[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html).


## Installation

There are two methods by which Desktop CMU Graphics is installable on a device:

- The [zip file installer](https://academy.cs.cmu.edu/desktop) that is available
for download on the CMU CS Academy website, and
- The version that is available on
[PyPI](https://pypi.org/project/cmu-graphics-test/) (Python Package Index) and
installable via PIP, Python’s built-in package-managing software.

Both versions come with their own advantages and limitations.

The zip file available on the website is designed to have a user-friendly
installation process for all users, and it should work regardless of most
software restrictions in place on school-distributed devices. With this
installer, the package can be used in three simple steps of downloading the
zipped folder, unzipping it, and moving the cmu_graphics folder to the location
of the Python file where you want to use the package. However, due to the method
by which dependencies are installed by the package, this version is only usable
on Windows and Mac devices. Additionally, in order to use this package with
Python files in multiple locations, the cmu_graphics folder must be either moved
or copied to each location in which it will be used.

For those using devices with Linux operating systems, or for those who are
familiar with the command line/terminal, the PIP installable version of the
package offers a larger degree of versatility. This version of the package can
be installed with the following command:

```
pip install cmu-graphics-test
```

The installation process that follows also downloads and installs all package
dependencies, so, like the zip file installer, no further installation steps are
required. This version allows you to install Desktop CMU Graphics directly to
your Python installation, meaning it can be used with any Python file you run
with the Python version that has the package installed. There is no need to
move or copy any files or directories. However, it requires a deeper
understanding of advanced tools for computer operation (i.e. the terminal),
and on school-provided devices, there may be restrictions in place that prevent
students or teachers from accessing the command line or terminal. When in doubt,
the zip file installer should work in almost all cases.

If neither of these installation approaches work for you, see the “Teacher
Support and Documentation” section below for more information about support
resources we provide.


## Getting Started

To run our graphics framework, include the following line at the top of your
Python file:

```
from cmu_graphics import *
```

From there, the syntax for using the graphics package is identical to the
online version of the framework.You can find more details about how to use the
graphics framework here on our [documentation page](https://academy.cs.cmu.edu/docs).


## Teacher Support and Documentation

If you are a teacher with a CMU CS Academy Account and you have questions about
CMU Graphics, remember that you can reach out to us through the Support tab on
the left side of the screen of your homepage on the CMU CS Academy website:

![Highlighted teacher support tab](https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/docs-media/support-tab.png)

If you are an educator but do not have an account with CMU CS Academy, you can
register for one at https://academy.cs.cmu.edu/register.

If you are a student, or you are exploring Desktop CMU Graphics,
there are plenty of resources to help you get started with
the framework. Students can reach out to their teachers for questions about
CMU Graphics, and a full reference documentation for the graphics
framework is available on our [documentation page](https://academy.cs.cmu.edu/docs).


## Replit

Desktop CMU Graphics is compatible with [Replit](https://replit.com/). To use
the package on the Replit website, follow the instructions on
[this document](https://docs.google.com/document/d/1Oj9L5n2MNJGuS8YpCeXJi4kouV74xD6LgvIjfSBmBbw/edit?usp=sharing).


## Dependencies

Desktop CMU Graphics depends upon the Pygame and Pycairo libraries for core
functionality like event handling and drawing. Additional functionality like
image processing and web requests depend on other smaller libraries. These
libraries should be installed automatically when you install this package via
pip, and they are already included within the
[zipped version of the package](https://academy.cs.cmu.edu/desktop).
Dependency versions:

- Pygame >= 2.0.0
- Pillow >= 7.2.0
- Certifi >= 2020.6.20
- Pycairo >= 1.20.0

## License

This package is distributed under the
[BSD-3-Clause license](https://spdx.org/licenses/BSD-3-Clause.html),
which can be found in the `LICENSE` file. CMU CS Academy and
Carnegie Mellon University reserve the right to publish later
versions of this package under a different license.