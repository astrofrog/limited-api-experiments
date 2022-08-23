#!/usr/bin/env python

import os

from setuptools import setup
from setuptools.extension import Extension

define_macros = [('CYTHON_LIMITED_API', '0x030800f0'),
                 ('Py_LIMITED_API', '0x030800f0')]

setup(ext_modules=[Extension("test_cython.example",
                             [os.path.join('test_cython', 'example.pyx')],
                             py_limited_api=True,
                             define_macros=define_macros)])
