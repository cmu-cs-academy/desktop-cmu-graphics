# Deploys package to PyPI
Set-Alias -Name python3 -Value c:/Users/taten/Downloads/tate-venv/Scripts/python.exe
cd C:\appveyor\applications\PypiUpload.zip
python3 -m install --upgrade build
python3 -m install --upgrade twine
python3 -m build
python3 -m twine upload --repository testpypi dist/*