#!/usr/bin/env python

import os

import numpy as np

from setuptools import setup
from setuptools.extension import Extension

setup(
    ext_modules=[
        Extension(
            "test_cython.example",
            [os.path.join("test_cython", "example.pyx")],
            py_limited_api=True,
            include_dirs=[np.get_include()],
            define_macros=[("Py_LIMITED_API", "0x030B0000")],
        ),
        Extension(
            "test_cython.pnpoly",
            [os.path.join("test_cython", "pnpoly.pyx")],
            py_limited_api=True,
            include_dirs=[np.get_include()],
            define_macros=[("Py_LIMITED_API", "0x030B0000")],
        )
    ]
)
