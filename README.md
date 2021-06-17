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

```
pip install cmu-graphics-test
```


## Getting Started

To run our graphics framework, include the following line at the top of your
Python file:

```
from cmu_graphics import *
```

From there, the syntax for using the graphics package is identical to the 
online version of the framework.


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
pip, and they are already included within the zipped version of the package. 
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