def fib(int n):
    cdef int a, b
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b
