def solution(weight, floor, top, max_p, max_w, bottom=1):
    stop_count = 0
    number_people = len(A)
    index = 0
    loop_count = 0
    
    _weight = 0
    _people = 0
    
    work_order = []

    while True:
        print index
        
        _weight += A[index]
        _people += 1

        if max_w >= _weight and max_p >= _people:
            work_order.append(B[index])
            index += 1
        else:
            work_order.append(bottom)
            _weight = 0
            _people = 0
        
        # check the last people
        if index >= number_people:
            work_order.append(bottom)
            break

    print "work_order:", work_order

    final_order = []
    while True:
        try:
            target = work_order.pop(0)
            if target == final_order[len(final_order) - 1]:
                continue
            final_order.append(target)
        except IndexError:
            if len(final_order) == 0:
                final_order.append(target)
                continue
            print "final_order done"
            break
    stop_count = len(final_order)

    print 'final_order: ', final_order
    print "stop_count: ", stop_count
    return stop_count


if __name__ == "__main__":
    import sys
    import random
    A = [60, 80, 40]
    B = [2, 3, 5]
    M = 5
    X = 2
    Y = 200
    try:
        num_test_run = sys.argv[1]
    except IndexError:
        num_test_run = 1000

    print solution(A, B, M, X, Y)
    M_N_X_MAX = pow(10, 5)
    Y_MAX = pow(10, 9)
    SIZE_MAX = pow(10, 3)

    for i in xrange(num_test_run):
        M = N = X = random.randrange(1, M_N_X_MAX)
        Y = random.randrange(1, Y_MAX)
        SIZE = random.randrange(1, SIZE_MAX)

        A = []
        B = []
        for i in xrange(SIZE):
            A.append(random.randrange(1, Y))
            B.append(random.randrange(1, M))

        solution(A, B, M, X, Y)
