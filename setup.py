from setuptools import setup, find_packages

s = setup(
    name="thingy-dl",
    version="0.0.1",
    license="GPL v3",
    description="Tool to automate Thingiverse file downloads",
    url='https://github.com/dsiguero/thingy-dl',
    packages=find_packages(),
    install_requires=[],
    python_requires=">= 3.7",
    author="Daniel Siguero",
    author_email="daniel.siguero@gmail.com",
)