import socket
from .utils import *
from .settings import *


def run_server():
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    cs, ca = s.accept()
    f = cs.makefile('rw')
    while True:
        q, answer = make_question()
        print(str_to_byte(q), file=f, flush=True)
        res = f.readline().replace('\n', '')
        if res == answer:
            print('Yes', file=f, flush=True)
        else:
            print('No', file=f, flush=True)


if __name__ == '__main__':
    run_server()
