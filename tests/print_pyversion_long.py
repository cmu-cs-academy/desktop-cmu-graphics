import platform
python_major, python_minor, _ = platform.python_version_tuple()
print(f"python{str(python_major)}.{str(python_minor)}")