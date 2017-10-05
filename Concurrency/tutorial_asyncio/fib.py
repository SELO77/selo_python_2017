from log_execution_time import log_execution_time


def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n


timed_fib = log_execution_time(fib)


# @log_execution_time
# def timed_fib(n):
#     return timed_fib(n - 1) + timed_fib(n - 2) if n > 1 else n


def pre_procedure(func):
    def wrapper(*args, **kwargs):
        print("start with:", args, kwargs)
        result = func(*args, **kwargs)
        print("end", result)
        return result
    return wrapper


@pre_procedure
def greet(name):
    print("Hello %s" % name)