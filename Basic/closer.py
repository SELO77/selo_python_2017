import sys
if 3 > sys.version_info.major:
    raise Warning('Run it on the Python3.')


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


def sort_priority3(values, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, val):
        if val in self.group:
            self.found = True
            return (0, val)
        return (1, val)


if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority(numbers, group)
    print('0: ', numbers)
    print('#################')

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    found = sort_priority2(numbers, group)
    print('1: ', numbers)
    print('1.1: ', found)
    print('#################')

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    found = sort_priority3(numbers, group)
    print('2: ', numbers)
    print('2.1: ', found)
    print('#################')

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sorter = Sorter(group)
    numbers.sort(key=sorter)
    print('3: ', numbers)
    print('3.1: ', sorter.found)
    assert  sorter.found is True

