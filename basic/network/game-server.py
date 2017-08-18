import socket
from gevent.server import StreamServer

from settings import *


users = {}


def add_user(cs, ):
    host, port = ca
    users.update({ca: {

    }})


def handle(cs, ca):
    cs.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    f = cs.makefile('rw')
    try:
        while True:
            print(f.readline())
            pass
    finally:
        pass


def run_server(host, port):
    print(host, port)
    server = StreamServer((host, port), handle=handle)
    server.serve_forever()


if __name__ == '__main__':
    run_server(host, port)