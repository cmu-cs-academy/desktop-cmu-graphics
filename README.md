![Desktop CMU Graphics Logo](/docs-media/pkg-logo.png)

Desktop CMU Graphics is an offline, desktop version of CS Academy Graphics, a 
persistent-object graphics package geared towards beginner computer science 
students. CS Academy Graphics and Desktop CMU Graphics are maintained by 
[CMU CS Academy](https://academy.cs.cmu.edu/splash), a free-to-use middle and 
high school computer science curriculum developed by Carngie Mellon University.

Desktop CMU Graphics works with **Python 3.6-3.9** and is compatible with
[Replit](https://replit.com/) (see "Replit" section below). This
package, including its documentation, is licensed under the 
[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html).


## Installation

```
pip install cmu-graphics-test
```


## Getting Started

To run our graphics framework, include the following line at the top of your
Python file:

```
from cmu_graphics import *
```

From there, the syntax for using the grahpics package is identical to the 
online version of the framework.


## Teacher Support and Documentation

If you are a teacher and you have questions about CS Academy Graphics or 
Desktop CMU Graphics, remember that you can reach out to us through the 
Support tab on the left side of the screen of your homepage on the CS
Academy website:

![img](/docs-media/support-tab.png)

If you are an educator but do not have an account with CS Academy, you can
register for one at https://academy.cs.cmu.edu/register.

If you are a student, or you are exploring Desktop CMU Graphics,
there are plenty of resources to help you get started with
the framework. Students can reach out to their teachers for questions about
CS Academy Graphics, and a full reference documentation for the graphics 
frameworks are available on our 
[documentation page](https://academy.cs.cmu.edu/docs).


## Replit

Desktop CMU Graphics is compatible with [Replit](https://replit.com/). To use
the package on the Replit website from the user homepage, click the dropdown 
icon located in the top-left corner of the screen. Note that this menu may
already by open be default:

![img](/docs-media/replit/step1.png)

From that menu, select "New Repl":

![img](/docs-media/replit/step2.png)

A prompt box will then appear, in which the user can select the language and 
name of their REPL. Select either "Python" or "Pygame" as the language and, optionally, name the REPL. Click "Create repl":

![img](/docs-media/replit/step3.png)
![img](/docs-media/replit/step4.png)

From there you will be directed to your REPL. From the icon menu on the left, 
select the cube icon for "Packages":

![img](/docs-media/replit/step5.png)

This will open a directory of packages that can be installed to the REPL. Type
"cmu-graphics-test" into the search bar. The package should be the first 
result. Select it:

![img](/docs-media/replit/step6.png)

The package description will then be shown. Click "Add" and wait for 
installation to complete in the shell in the lower left corner of the screen.
The button should change from a green "Add" button to a red "Remove" button
when the installation is complete: 

![img](/docs-media/replit/step7.png)

After installing the package, you should be able to run any Python file using 
Desktop CMU Graphics inside of your REPL.


**(Optional) Removing Linter Warnings**

Replit uses PyFlakes to lint Python files and check for potential error sources
before running your file. PyFlakes raises a warning (denoted by green squiggly
lines under your code) when it encounters star imports, which is what Desktop
CMU Graphics uses to import all of its shapes and functions. If you would like to
remove these warnings, navigate to the Settings menu on the left side of your
REPL:

![img](/docs-media/replit/optional1.png)

Scroll down to the bottom of the menu that appears and set "Code 
intelligence" to "disabled":

![img](/docs-media/replit/optional2.png)

This should remove the linter warnings from your code. However, please note 
that selecting this option will also turn off Autocomplete, hints, and other
similar features that Replit provides.



## Dependencies


Desktop CMU Graphics is heavily dependent upon the Pygame and 
Pycairo graphics libraries. Additional functionality like image
processing and other backend features depend on other smaller 
libraries. These libraries should be installed automatically when
you install this package via pip, and they are already included within
the zipped version of the package. Dependency versions:

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

Basically, this means that if you use our package in a personal 
or business project, and you share/distribute our package with
that project, you must include the license with its copyright to
Carnegie Mellon University in that distribution. Furthermore, 
you may not use Carnegie Mellon University, CMU CS Academy, or any 
of this package's developers to promote your product unless you 
receive explicit written consent from them to do so.