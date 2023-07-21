![Desktop CMU Graphics logo](https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/docs-media/pkg-logo.png)

Desktop CMU Graphics is an offline version of CMU Graphics, a
persistent-object graphics package geared towards beginner computer science
students. CMU Graphics and its desktop version are maintained by
[CMU CS Academy](https://academy.cs.cmu.edu/), a Carnegie Mellon University
project which develops free-to-use middle and high school computer science
curriculum.

Desktop CMU Graphics works with **Python 3.6-3.11** and is compatible with
[Replit](https://replit.com/) and [Coding Rooms](https://www.codingrooms.com/)
(see the "Replit" and "Coding Rooms" sections below). This
package, including its documentation, is licensed under the
[BSD 3-Clause license](https://github.com/cmu-cs-academy/desktop-cmu-graphics/blob/master/LICENSE).


## Installation

### Choose zip or pip

There are two different ways to install Desktop CMU Graphics on a device:

1. (Mac and Windows only) Use the [zip file installer](https://academy.cs.cmu.edu/desktop) that is available
for download on the CMU CS Academy website.
1. (Mac, Windows, and Linux) Use pip, Python’s built-in package-managing software.

Both methods come with their own advantages and limitations. If you're in doubt
about which to choose, the zip file installer is the most likely to succeed. It
should work regardless of most restrictions in place on school-distributed devices.

For those using devices with Linux operating systems, or for those who are
familiar with the command line/terminal, the pip version of the
package offers a larger degree of versatility.

The remainder of these installation instructions are only for the pip version.

### Install dependencies

If you're using Windows, you don't need to install any dependencies. Skip ahead to "Install CMU Graphics" below.

If you're using a Mac, install [Homebrew](https://brew.sh/).

If you're using a Mac or Linux, install the software packages needed by pycairo. Read their [getting started page](https://pycairo.readthedocs.io/en/latest/getting_started.html) for instructions.

### Install CMU Graphics

Run the following command:

```
pip install cmu-graphics
```

## Getting Started

To run our graphics framework, include the following line at the top of your
Python file:

```
from cmu_graphics import *
```

At the end of your Python file, add this line:

```
cmu_graphics.run()
```

From there, the syntax for using the graphics package is identical to the
online version of the framework. You can find more details about how to use the
graphics framework here on our [documentation page](https://academy.cs.cmu.edu/docs).


## Teacher Support and Documentation

If you are a teacher with a CMU CS Academy Account and you have questions about
CMU Graphics, remember that you can reach out to us through the Support tab on
the left side of the CMU CS Academy website:

![Highlighted teacher support tab](https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/docs-media/support-tab.png)

If you are an educator but do not have an account with CMU CS Academy, you can
[register for an account here](https://academy.cs.cmu.edu/register).

If you are a student, or you are exploring Desktop CMU Graphics,
there are plenty of resources to help you get started with
the framework. Students can reach out to their teachers for questions about
CMU Graphics, and a full reference documentation for the graphics
framework is available on our [documentation page](https://academy.cs.cmu.edu/docs).


## Replit

Desktop CMU Graphics is compatible with [Replit](https://replit.com/). To use
the package on the Replit website:

1. Create a new repl. Choose "Python-CMUGraphics" as the language.
1. Run your code!

## Coding Rooms

Desktop CMU Graphics is compatible with [Coding Rooms](https://www.codingrooms.com/). To use the package on the
Coding Rooms website:

1. Visit [this link](https://www.codingrooms.com/compiler/python3) to create a workspace
1. Click "Start Coding Python for Free Now"
1. Click the blue "View Desktop" button above the shell
1. Run your code!