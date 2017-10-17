import time
import sys


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


def tail_f(f, target):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.2)
            continue
        elif ':exit' in line:
            return
        target.send(line)


@coroutine
def grep(pattern, target):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)


print_count = 0


@coroutine
def printer():
    global print_count
    print_count += 1
    print('Open a printer id: %d.' % print_count)
    while True:
        line = (yield)
        print(line)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        p = printer()
        g = grep('python', p)
        tail_f(f, g)


    # 위 코드 flow
    # main grep tail_f
    # 라인이 있을경우 grep
            # 패턴이 있을경우 main
            # 패턴이 없을경우 tail_f
    # 라인이 없을 경우 tail_f

if __name__ == '__main__':
    main()

