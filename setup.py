import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmu-graphics-test",
    version="1.1.3",
    author="Austin Schick",
    author_email="aschick@andrew.cmu.edu",
    description="The graphics framework used by CMU CS Academy, geared toward beginner CS students.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://academy.cs.cmu.edu/",
    project_urls={
        "Documentation": "https://academy.cs.cmu.edu/docs",
    },
    license = "BSD 3-Clause License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "pygame>=2",
        "Pillow>=7.2",
        "certifi>=2020.6.20",
        "pycairo>=1.20"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6, <4",
)
