#!/usr/bin/env python

import os

import numpy as np

from setuptools import setup
from setuptools.extension import Extension

define_macros = [
    ("CYTHON_LIMITED_API", "1"),
    ("Py_LIMITED_API", "0x030C0000"),
]

setup(
    ext_modules=[
        Extension(
            "test_cython.example",
            [os.path.join("test_cython", "example.pyx")],
            py_limited_api=True,
            include_dirs=[np.get_include()],
            define_macros=define_macros,
        )
    ]
)
