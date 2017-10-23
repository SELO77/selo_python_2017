from threading import Thread
from time import (
    time,
    sleep
)
from fib import timed_fib


def print_hello():
    while True:
        print('{} - Hello world!'.format(int(time())))
        sleep(3)

def read_and_process_input():
    while True:
        n = int(input("Input:"))
        print('fib({}) = {}'.format(n, timed_fib(n)))


def main():
    # Second thread will print "hello world".
    # Starting as a daemon means the thread will not prevent the process form exiting
    t = Thread(target=print_hello)
    t.daemon = True
    t.start()

    read_and_process_input()


if __name__ == '__main__':
    main()
