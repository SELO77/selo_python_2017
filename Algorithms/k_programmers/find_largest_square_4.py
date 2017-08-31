# O와 X로 채워진 표가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
# 표에서 O로 이루어진 가장 큰 정사각형을 찾아
# 넓이를 반환하는 findLargestSquare 함수를 완성하세요.

def view_board(board):
    for row in board:
        for e in row:
            print(e, end='')
        print()

def findLargestSquare(board):
    answer = 0
    view_board(board)

    for y, row in enumerate(board):
        for x, e in enumerate(row):
            if e == 'X':
                continue
            else:
                print()
                pass

    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))