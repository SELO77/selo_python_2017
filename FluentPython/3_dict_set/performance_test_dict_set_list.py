from timeit import timeit

# t = [v for v in range(10000) if v%2 == 0]
st = timeit('t = [v for v in range(10000) if v%2 == 0]')
# print(st)
print(timeit())

# print(timeit()-st)