cd ../../pypi_upload

python -m build
python -m twine upload dist/*