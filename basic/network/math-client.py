import socket
from functools import reduce


from settings import *


def run_client():
    s = socket.socket()
    s.connect((host, port))
    while True:
        f = s.makefile('rw')
        print(f.readline())
        # q = res.decode()
        # answer = reduce(lambda x, y: x + y, q.split('+'))
        answer = input('Input answer:')
        print(answer, file=f, flush=True)
        print(f.readline())

if __name__ == '__main__':
    run_client()


# reuse addr