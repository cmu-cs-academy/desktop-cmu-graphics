# Deploys package to PyPI
cd C:\appveyor\applications\PypiUpload.zip
py -m install --upgrade build
py -m install --upgrade twine
py -m build
py -m twine upload --repository testpypi dist/*