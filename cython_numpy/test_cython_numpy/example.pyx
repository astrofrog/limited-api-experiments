cimport cython
import time
import numpy
cimport numpy
cimport cython

ctypedef numpy.float_t DTYPE_t

def fib(int n):
    cdef int k
    cdef numpy.ndarray[DTYPE_t, ndim=1] arr=numpy.zeros(n, dtype=float)
    arr[0] = 0
    arr[1] = 1
    for k in range(2, n):
        arr[k] = arr[k - 1] + arr[k - 2]
    return arr
