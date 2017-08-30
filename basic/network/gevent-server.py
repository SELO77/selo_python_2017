from gevent.server import StreamServer
from utils import *
from settings import *


def handler(cs, ca):
    f = cs.makefile('rw')
    while True:
        q, answer = make_question()
        print(str_to_byte(q), file=f, flush=True)
        res = f.readline().replace('\n', '')
        if res == answer:
            print('Yes', file=f, flush=True)
        else:
            print('No', file=f, flush=True)


def main():
    server = StreamServer((host, port), handle=handler)
    server.serve_forever()


if __name__ == '__main__':
    main()