def fib(n):
    if 2 > n:
        return n
    return fib(n - 1) + fib(n - 2)


# 1 1 2 3 5 8 13
# fib(0) => 0
# fib(1) => 1
# fib(2) => fib(1) + fib(0) => 1
# fib(3) => fib(2) + fib(1) => 2
# fib(4) => fib(3) + fib(2) => 3
# fib(5) => fib(4) + fib(3) => 5

from functools import wraps
from time import time

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time()
        result = func(*args, **kwargs)
        duration = time() - st
        print("Executing {} took {:.03} seconds.".format(func.__name__, duration))
        return result
    return wrapper

timed_fib = log_execution_time(fib)