import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("cmu_graphics/meta/version.txt", "r", encoding="utf-8") as f:
    version = f.read().strip()

setuptools.setup(
    name="cmu-graphics",
    version=version,
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
    packages=["cmu_graphics", "cmu_graphics.samples", "cmu_graphics.libs"],
    package_data={"cmu_graphics": ["meta/version.txt"]},
    python_requires=">=3.6, <4",
)
