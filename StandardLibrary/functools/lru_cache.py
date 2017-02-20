from functools import lru_cache

count = 0
#@lru_cache(maxsize=32)
def fib(n):
    global count
    count += 1
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print(fib(5))
print(count)
count = 0
print(fib(3))
print(count)
# print([fib(n) for n in range(10)])
