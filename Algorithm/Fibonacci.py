def fibonacci(num, a=1):
    if num < 2: raise IndexError('Start num is over 2. Given num is %d' % num)
    a, b, count = 1, 1, 1
    if count == num: return b
    else:
        a, b = b, a + b
        count += 1


def fibonacci2(num, a=1, b=1, count=2):
    if num > 1:
        if num == count: return b
        a, b = b, a + b
        count += 1
        return fibonacci2(num, a, b, count)
    elif num == 0: return 0
    elif num == 1: return 1
    else:
        raise TypeError

import time
st = time.time()

num = int(input('Input positive integer for fibonacci >'))

print(fibonacci2(num))

duration = time.time() - st
print(duration)

from datetime import datetime

message = 'ts: %d, num: %d, duration: %.2f' \
          % (datetime.timestamp(datetime.utcnow()), num, duration)
print(message)
with open('fibonacci.log', 'w+') as f:
    f.write(message)