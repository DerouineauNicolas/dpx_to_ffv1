from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dpx2ffv1',
    description='dpx2ffv1 is a simple module to convert a set of dpx to ffv1 codec',
    version='0.1.0',
    url='https://github.com/DerouineauNicolas/dpx_to_ffv1',
    author='N. DEROUINEAU',
    author_email='nicolas.derouineau@ymagis.com',
    license='WTFPL',
    package_dir={'dpx2ffv1': 'dpx2ffv1'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(),
    entry_points={'console_scripts': ['Package = dpx2ffv1.__main__:main']})
