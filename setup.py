from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dpx2ffv1',
    package_dir={'dpx2ffv1': 'src'},
    packages=find_packages(),
    entry_points={ 'console_scripts': ['Package = src.__main__:main' ] })