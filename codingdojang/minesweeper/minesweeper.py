# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고
# 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다.
# 이때 2차원 리스트 안에서 * 은 지뢰이고 .은 지뢰가 아닙니다.
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요.

from random import *

print("시작할 행과 열을 입력해주세요.")
col, row = map(int, input("> ").split())

matrix = []

for i in range(row):
    matrix_in = []
    for j in range(col):
        num = randrange(0, 10)
        if num >= 5:
            num = '*'
        else:
            num = '.'
        matrix_in.append(num)
        print(num, end='')
    print()
    matrix.append(matrix_in)

count = 0

for i in range(len(matrix)):
    for j in range(len(matrix_in)):
        if j == 0:
            if matrix[i][j] != '*' and matrix[i][j + 1] == '*':
                count = count + 1
                matrix[i][j] = count
            else:
                count = 0
                continue

        if j == 1:
            if matrix[i][j] != '*' and matrix[i][j + 1] == '*' or matrix[i][j - 1] == '*':
                count = count + 1
                matrix[i][j] = count
            else:
                count = 0
                continue

        if j == 2:
            if matrix[i][j] != '*' and matrix[i][j - 1] == '*':
                count = count + 1
                matrix[i][j] = count
            else:
                count = 0
                continue

print(matrix)