#!/usr/bin/env python

from setuptools import setup
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

# extra_files = package_files('amipy/package_template')
extra_files = []

with open('README.md') as f:
    readme = f.read()

setup(
    name='amipy',
    version='1.0.35',
    description='PythonAutomation for Amibroker', # short description
    long_description=readme, # long description from the readme file
    license='MIT', # for internal packages
    author='Chen Huang',
    author_email='chinux@gmail.com',
    url='https://github.com/chinux23/amipy', # wherever your code lives
    packages=['amipy'], # or py_modules (see below for more details)
    package_data={'maui': extra_files},
    # data_files=[('package_template', ['*.jpeg'])],
    # include_package_data=True,
    install_requires = [
        "win32com",
    ], # any dependencies internal or world (OPTIONAL)
    entry_points={
        'console_scripts': [
            'amipy = amipy.amipy:main',
        ]
    }
)