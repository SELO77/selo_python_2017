from gevent.server import StreamServer
from settings import *


users = []


def handler(cs, ca):
    f = cs.makefile('rw')
    print('chat start', file=f, flush=True)
    users.append(f)

    try:
        while True:
            # if connected_socket:
            res = f.readline()
            print(res)
            for u in users:
                if u != f:
                    print(res, file=u, flush=True)
    finally:
        users.remove(f)

    # if connected_socket:
    #     for each in connected_socket:
    #         res = each.readline()
    #         print(res)
    #         print(each.readline(), file=f, flush=True)


def main():
    server = StreamServer((host, port), handle=handler)
    print(host, port)
    server.serve_forever()


if __name__ == '__main__':
    main()