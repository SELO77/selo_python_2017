#!/bin/local/python2
from functools import wraps


class SeloDict(dict):
    pass

def memorize(func):
    memo = SeloDict()
    @wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = func(*args)
            memo[args] = rv
            return rv
    return wrapper


count = 0
@memorize
def fibonacci(n):
    global count
    count += 1
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci2(n):
    global count
    count += 1
    if n < 2: return n
    return fibonacci2(n-1) + fibonacci2(n-2)
