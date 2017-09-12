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


from itertools import permutations


def findLargestSquare(board):
    n = 0
    answer = pow(n, 2)
    board_size = len(board)
    view_board(board)

    check_board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    print(check_board)

    def check(r, c, size=0):
        if r == c == board_size - 1:
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




#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(next(findLargestSquare(testBoard)))