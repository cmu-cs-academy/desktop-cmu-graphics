# Testing

To run the tests, create and activate a virtual environment:

    python3 -m virtualenv venv
    source venv/bin/activate

Then install some dependencies:

    python -m pip install twine build tox

Build the pip and zip packages:

    python build/build.py

Run the tests:

    python -m tox

# Translation

Translation into Spanish and German is handled by a library.
You don't need to edit the content between `# start_translate` and `# end_translate`.
