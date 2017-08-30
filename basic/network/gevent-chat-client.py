import socket

from settings import *


def run_client():
    s = socket.socket()
    s.connect((host, port))
    f = s.makefile('rw')
    while True:
        print(f.readline())
        req = input('input>>')
        print(req, file=f, flush=True)


if __name__ == '__main__':
    run_client()