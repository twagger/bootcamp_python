#!/bin/bash

# Get / Update build packages
python -m pip install --upgrade pip setuptools wheel twine

# Build the package
python3 -m build

# Build the .egg format
python setup.py bdist_egg

# Install the package
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl

# Clean the build folder
rm -rf ./build