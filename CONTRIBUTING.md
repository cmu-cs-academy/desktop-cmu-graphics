# Getting started

#### 1. [Have a GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
#### 2. Download the following programs on your os:

- GIT: https://git-scm.com/downloads
- Python: https://www.python.org/downloads/
- An IDE (we recommend PyCharm or VSCode)

You may also find yourself prompted to install cmake and-or zlib at some point, but if not don't worry about it.
#### 3. [Fork the repo to your own GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)
#### 4. [Clone the repo or download it as a zip on your local machine](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)
### 5. Explore!!

# Project Structure

#### - Desktop-cmu-graphics should be your main folder.
#### - Inside of it you will find some files that are not part of the library itself but that are useful to develop and maintain it. Spend about 5-10min exploring these and come back here, we will go over them one by one when needed.
#### - You will also find multiple folders but the 3 that you need to pay attention to are cmu_graphics, the actual library code, test and samples that will give you an insight on what this library does and how to operate it.
#### - The files inside cmu_graphics folder are the most important to understand; Here they are ordered in terms of there relative importance:
- cmu_graphics.py
- shape_logic.py
- utils.py
- \_\_init__.py
- sound.py
- modal.py (you very rarely are going to touch the last 2...)

# Start developing

#### In your terminal navigate to desktop-cmu-graphics folder (all the following command to execute in the terminal will be from desktop-cmu-graphics, except otherwise specified)

- `cd ~`
- `ls`
- `cd <path/to/desktop-cmu-graphics>`

#### Create and activate a virtual environment:

    python -m virtualenv venv
    source venv/Scripts/activate (if on Windows)
    source venv/bin/activate     (otherwise)

#### Then install some dependencies:

    pip install twine build tox

#### [Then install some more...😅](https://github.com/cmu-cs-academy/desktop-cmu-graphics?tab=readme-ov-file#install-dependencies)

#### Then install cmu_graphics as editable:
    pip install -e .
(this will likely fail so in desktop-cmu-graphics/setup.py on line 33 remove "cmu_graphics.samples",)

###### Now there might be files that are changed that you don't want git to track. Sometimes adding that file to .gitignore will work, but in case it doesn't run the following command:
    git update-index --assume-unchanged <filename>
###### and if you want to track it again run:
    git update-index --no-assume-unchanged <filename>

### That's it you should be set!!

That being said, before changing anything, setup your testing environment; you won't use it directly but doing so now will eliminate the possibility that your change is what is failing the tests.

# Testing

#### On your first time only you will have to
- Build the pip and zip packages:

      python build/build.py

- Install testing dependencies:

      pip install psutil pillow imageio numpy

- Run tox:

      tox

###### After the first time of running tox successfully, we recommend you changing your tox.ini file to only run the tests once, by restricting the interpreters to one that worked the first time.
###### For example, the second line should go from something like this:
`envlist=py{38,39,310,311,312}-{pip,zip}`
###### To something like this:
`envlist=py{311}-{pip}`

#### Each following time you want to run the tests use the `tox` command in your terminal.

# Using the test output

#### If tox gives an error, try running the specific test that failed.
###### (it's going to be one of test_get_text_input.py, test_sound.py and test_image_gen.py all located under desktop-cmu-graphics/tests)
###### The one that is most likely to fail is test_image_gen.py.

#### To run one of the tests in isolation:

    python tests/<test_name>

#### If it doesn't fail, then tox is probably wrong and you can safely go to the next step.

#### If on the other hand it fails, it will give you a `report.html` file that contains info on the sub-tests that failed.
##### `report.html` should have 3 images on top (correct image, output image and difference image respectively) as well as the entire test code. Copy that test code in a new python file and run it to get to the place that threw the error. From there happy debugging.
###### Final tip, if you want to run test_image_gen.py again delete the generated image_gen folder to avoid it crashing at you.

# Making changes

### The best way is as follow:

#### 1. Branching: Create a new branch with a simple descriptive name (e.g., new_feature_\<feature name>).

###### Use GitHub's website, VSCode UI, or CLI (git checkout <branch name>).

#### 2. Making Changes: Implement your changes locally on the branch. Use multiple short and descriptive commits. And test your code!!

#### 3. Pushing Changes: Push commits to GitHub using VSCode UI or git push.

#### 4. Pull Request (PR):

- [Open a PR on GitHub.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
- Include details like what's changed and why.
#### 5. Review and Feedback: We'll review your PR and provide feedback if needed.

### 6. Completion: Once approved, you've contributed! BIG THANKS!!!

###### Note: This document was mostly made by a person using Windows and VSCode. Please let us know of any differences or improvements for other OS and editors. Best way to notify us of any problem or propose improvement is by opening a new issue (at the top of the library's GitHub page).

###### PS: If you have made it this far, please email mshikfa@andrew.cmu.edu once with subject: `Important Lemon Melon` and body: `🍋🍈`, I wonder how many I will get😅🤔.
