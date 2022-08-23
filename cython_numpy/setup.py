#!/usr/bin/env python

import os
import sys

import numpy

from setuptools import setup
from setuptools.extension import Extension

define_macros = [('CYTHON_LIMITED_API', '0x030800f0'),
                 ('Py_LIMITED_API', '0x030800f0'),
                 ('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]

setup(ext_modules=[Extension("test_cython_numpy.example",
                             [os.path.join('test_cython_numpy', 'example.pyx')],
                             py_limited_api=True,
                             define_macros=define_macros,
                             include_dirs=[numpy.get_include()])])
