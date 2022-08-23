#!/usr/bin/env python

import os
import sys

from setuptools import setup
from setuptools.extension import Extension

setup(ext_modules=[Extension("test_cython.example",
                             [os.path.join('test_cython', 'example.pyx')],
                             py_limited_api=True)])
