# from collections import OrderedDict
# d = {"name": "selo", "sex": "m", "age": 31}
#
# QUERY = "INSERT INTO TN (%s) VALUES (%s)"
#
# fields = ""
# values = ""
#
# for k, v in d.items():
#     fields += '%s, ' % k
#     values += '%s, ' % v
#
# query = QUERY % (fields, values)
# print(query)
#
# print(list(zip(d.items())))

import random
import threading
import sys
import itertools


write = sys.stdout.write
flush = sys.stdout.flush


flag = True


def check_dict():
    random_pool = list(range(20))
    global flag
    for _ in range(1000000):
        d = {}
        for __ in range(5):
            key = str(random.choice(random_pool))
            val = str(random.choice(random_pool))
            d.update({key: val})

        keys = list(d.keys())
        vals = list(d.values())

        for i in range(len(d)):
            if d[keys[i]] != vals[i]:
                flag = False
                return "Fuck"
    flag = False
    return "SUUUU"


def spin():
    import time
    global flag
    for char in itertools.cycle('|/-\\'):
        status = char + ' '
        write(status)
        flush()
        time.sleep(0.2)
        write('\x08' * len(status))
        if not flag:
            return



if __name__ == "__main__":
    t = threading.Thread(target=spin)
    t.start()
    print(check_dict())
    t.join()