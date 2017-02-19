from timeit import timeit


def make_list_1():
    result = []
    for value in range(1000):
        result.append(value)
    return result


def make_list_2():
    result = [value for value in range(1000)]
    return result


print('first', timeit(make_list_1, number=1000))
print('second', timeit(make_list_2, number=1000))
