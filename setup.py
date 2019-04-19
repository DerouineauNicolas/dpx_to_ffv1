from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dpx2ffv1',
    package_dir={'dpx2ffv1': 'dpx2ffv1'},
    packages=find_packages(),
    entry_points={ 'console_scripts': ['Package = dpx2ffv1.__main__:main' ] })