import sys
from setuptools import setup

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

setup(
    name='opencv-python',

    # Use the same version as opencv-python-headless
    version=metadata.version('opencv-python-headless'),
)
