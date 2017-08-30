import random


def make_question():
    a = random.randrange(10)
    b = random.randrange(10)
    c = str(a + b)
    return (f'{a}+{b}', c)


def str_to_byte(a):
    return a.encode()