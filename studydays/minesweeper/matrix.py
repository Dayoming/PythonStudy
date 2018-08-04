"""
숙제
- 게임판의 크기를 지정하도록 변경
- 게임판의 크기에 따라 지뢰의 갯수 변경
- 지뢰 표시 기능 추가
- 지뢰의 위치를 저장한 리스트를 따로 사용하고 매트릭스는 하나만 사용하도록 수정
"""
import sys
import time
from random import randrange

# 게임판의 크기 지정
print("게임판의 크기를 입력해주세요.")
matrix_i_length, matrix_j_length = map(int, input("> ").split())

mine = matrix_i_length

result_matrix = []
for i in range(matrix_i_length):
    result_matrix_list = []
    for j in range(matrix_j_length):
        result_matrix_list.append('+')

    result_matrix.append(result_matrix_list)


# 게임판의 크기에 따라 지뢰의 갯수 변경
mine_matrix = []
for i in range(matrix_i_length):
    mine_matrix_list = []
    num = randrange(0, matrix_j_length)
    for j in range(matrix_j_length):
        if j == num:
            mine_matrix_list.append('*')
        else:
            mine_matrix_list.append('+')
    mine_matrix.append(mine_matrix_list)

print(mine_matrix)


def mine_counter(row_index, column_index):
    """
    주변 9칸의 지뢰 갯수를 찾는 함수
    row_index = 2
    column_index = 2
    라고 가정했을 때 확인해야할 인덱스들

    (-1, -1) (-1, -) (-1, +1)
     (-, -1)  (2, 2)  (-, +1)
    (+1, -1) (+1, -) (+1, +1)
    """

    # 확인하려는 인덱스의 값이 지뢰일때는 바로 반환
    if mine_matrix[row_index][column_index] == '*':
        return '*'

    # 확인할 인덱스 생성
    row = [row_index - 1, row_index, row_index + 1]
    column = [column_index - 1, column_index, column_index + 1]

    mine_count = 0

    for i in row:
        for j in column:
            if row_index == row and column_index == column:
                continue

            if 0 <= i < matrix_i_length and 0 <= j < matrix_j_length:
                if mine_matrix[i][j] == '*':
                    mine_count = mine_count + 1
                else:
                    result_matrix[i][j] = '.'
        # print()
    return mine_count


# 지뢰 출력
def view_matrix():
    for i in range(matrix_i_length):
        for j in range(matrix_j_length):
            print("{0:>2}".format(result_matrix[i][j]), end="")
            # 문자열 포맷 두자리 오른쪽 정렬 줄바꿈 없음
        print()


def end_game(user_input):
    if 'Q' == user_input.upper():
        print("게임을 그만합니다.")
        sys.exit(0)


def get_row_and_column(index):
    index = index - 1
    row = index // matrix_i_length
    # 나누기 연산 후 소수점 아래의 숫자를 버리고 정수만
    column = index % matrix_i_length
    return row, column


def found_mine_counter():
    plus_count = 0

    for i in range(matrix_i_length):
        for j in range(matrix_j_length):
            if result_matrix[i][j] == '+':
                plus_count = plus_count + 1

    return plus_count == mine

# 의심 지뢰 체크가 실제 지뢰 위치와 일치하는지 확인
def check_mine(i, j):
    check_count = 0

    if mine_matrix[i][j] == '*':
        check_count = check_count + 1
    result_matrix[i][j] = '?'

    return check_count


def main():
    start_time = time.time()
    check_count = 0

    while True:
        view_matrix()

        user_input = input('> ')

        end_game(user_input)

        if user_input.count('?') > 0:
            i, j = get_row_and_column(int(user_input.replace('?', '')))
            check_count = check_count + check_mine(i, j)
        else:
            i, j = get_row_and_column(int(user_input))
            mine_count = mine_counter(i, j)

            if mine_count == 0:
                result_matrix[i][j] == '.'
            else:
                result_matrix[i][j] = mine_count

            if mine_count == '*':
                view_matrix()
                print("지뢰를 밟았습니다!")
                end_time = time.time()
                print(int(end_time - start_time), "초 경과")
                sys.exit(0)

        if found_mine_counter() or check_count == mine:
            view_matrix()
            print("모든 지뢰를 찾았습니다.")
            end_time = time.time()
            print(int(end_time - start_time), "초 경과")
            sys.exit(0)


if __name__ == '__main__':
    main()