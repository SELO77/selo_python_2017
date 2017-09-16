# O와 X로 채워진 표가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
# 표에서 O로 이루어진 가장 큰 정사각형을 찾아
# 넓이를 반환하는 findLargestSquare 함수를 완성하세요.

def view_board(board):
    print(' ', end='')
    for i in range(len(board)): print(i, end='')
    print()
    row_index = 0
    for row in board:
        print(row_index, end='')
        for e in row:
            print(e, end='')
        row_index += 1
        print()


def mark_2_check_board(r, c, check_board):
    check_board[r][c] = 'X'


def findLargestSquare(board):
    n = 0
    answer = pow(n, 2)
    board_size = len(board)
    view_board(board)

    check_board = [['O' for _ in range(board_size)] for _ in range(board_size)]
    print('===============')

    def check(r, c, size=0):
        mark_2_check_board(r, c, check_board)

        if r == c == board_size - 1:
            view_board(check_board)

            yield size

        if board[r][c] == 'X':
            if r == c:
                yield from check(r+1, c, size)
            else:
                yield from check(r, c+1, size)
        else:
            if size == 0: size = 1

            for i in range(1, size + 1):
                for j in range(1, size + 1):
                    if board[r + i][c + j] == 'X':
                        yield from check(r + i, c + j, size)

            if r == c:
                yield from check(r+1, c, size)
            else:
                yield from check(r, c+1, size)

    yield from check(0, 0)


###################################################
def check_square(x, y, length, board):
    if 2 > length :
        return True
    d = length - 1
    try:
        for i in range(0, d):
            v = board[x + d][y + i]
            if v == 'O':
                continue
            else:
                return False

        for j in range(0, d):
            v = board[x + j][y + d]
            if v == 'O':
                continue
            else:
                return False

        if board[x + d][y + d] == 'O':
            return True
    except IndexError:
        return False
    return False


def findLargestSquare2(board):
    n = 0
    r_length = len(board)
    view_board(board)
        # print("check_square function is wrong. It must be fixed.")

    for x, r in enumerate(board):
        for y, c in enumerate(r):
            if c == 'X':
                continue
            elif c == 'O':
                if n == 0:
                    n = 1
                for l in range(2, r_length):
                    if check_square(x, y, l, board):
                        if l > n:
                            n = l
                    else:
                        break
    print('last n:', n)
    return pow(n, 2)

#아래 코드는 출력을 위한 테스트 코드입니다.
testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
testBoard2 = [['X','O','O','O','X', 'O'],['X','O','O','O','O','O'],['X','X','O','O','O','O'],['X','X','O','O','O', 'O'],['X','X','X','X','X','O'],['X','X','O','O','O','O'],]
assert check_square(0, 1, 2, testBoard) == True
assert check_square(0, 1, 1, testBoard) == True
assert check_square(0, 1, 3, testBoard) == False
print(findLargestSquare2(testBoard)) # 9
print(findLargestSquare2(testBoard2)) # 9
# print(next(findLargestSquare(testBoard))) # 9