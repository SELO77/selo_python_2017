import time
import sys
#
#
# def tail_f(f):
#     f.seek(0, 2)
#     while True:
#         line = f.readline()
#         if not line:
#             time.sleep(0.1)
#             continue
#         yield line
#
#
# def main():
#     filename = "log"
#     # logfile = open(filename)
#     with open(filename) as f:
#         for line in tail_f(f):
#             print(line)

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


def tail_f(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.2)
            continue
        yield line


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


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
        new_lines = tail_f(f)
        grep_lines = grep('python', new_lines)
        pr = printer()
        for line in grep_lines:
            pr.send(line)

    # 위 코드 flow
    # main grep tail_f
    # 라인이 있을경우 grep
            # 패턴이 있을경우 main
            # 패턴이 없을경우 tail_f
    # 라인이 없을 경우 tail_f

if __name__ == '__main__':
    main()

