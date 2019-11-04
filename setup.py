import pathlib

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

s = setup(
    name="thingy-dl",
    version="0.0.1",
    license="GPL v3",
    description="Tool to automate Thingiverse file downloads",
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/dsiguero/thingy-dl',
    packages=find_packages(),
    install_requires=[],
    python_requires=">= 3.7",
    author="Daniel Siguero",
    author_email="daniel.siguero@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "thingy-dl=thingy_dl.__main__:main",
        ]
    },
)