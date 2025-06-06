#!/usr/bin/env python

import os

from setuptools import setup
from setuptools.extension import Extension

setup(
    ext_modules=[
        Extension(
            "test_cython.example",
            [os.path.join("test_cython", "example.pyx")],
            py_limited_api=True,
            define_macros=[("Py_LIMITED_API", "0x030B0000")],
        ),
        Extension(
            "test_cython.utils",
            [os.path.join("test_cython", "utils.pyx")],
            py_limited_api=True,
            define_macros=[("Py_LIMITED_API", "0x030B0000")],
        )
    ]
)
