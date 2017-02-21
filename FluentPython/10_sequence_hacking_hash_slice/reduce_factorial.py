import functools


x = functools.reduce(lambda a, b: a*b, range(1,6))
print(x)


n = 0
for i in range(6):
    n ^= i
print(n)
