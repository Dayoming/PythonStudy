# 함수, 튜플, 딕셔너리를 사용해 숫자야구 게임 만들기
from random import *

def print_message(num): # 딕셔너리 사용
    input_number = {0: "> 첫 번째 숫자를 입력하세요.",
                    1: "> 두 번째 숫자를 입력하세요.",
                    2: "> 세 번째 숫자를 입력하세요."}

    print(input_number[num])

def count_score(tuple1, tuple2): # 튜플 사용
    strike_count = 0
    ball_count = 0

    for i in range(baseball_number_length):
        if tuple1[i] == tuple2[i]:
            strike_count = strike_count + 1
        elif tuple1.count(tuple2[i]) > 0:
            ball_count = ball_count + 1

    return strike_count, ball_count


baseball_number_length = 3
numbers = []
index = 0

while index < baseball_number_length: # index가 baseball_number_length보다 작은 동안
    numbers.append(randrange(0, 10)) # 0부터 9까지 랜덤 수 1개 저장
    has_duplicate = False

    for i in (range(index)):
        if numbers[index] == numbers[i]:
            has_duplicate = True
            numbers.pop()
            break

    if not has_duplicate:
        index = index + 1

numbers_tuple = tuple(numbers)

print("> 수비수가 고른 숫자")
for number in numbers:
    print(number)

guess_numbers = []

while True:
    guess_numbers.clear()

    for i in range(baseball_number_length):
        print_message(i)
        guess_numbers.append(int(input("prompt> ")))

    guess_numbers_tuple = tuple(guess_numbers)

    print("> 공격수가 고른 숫자")

    for i in range(baseball_number_length):
        print(guess_numbers[i])

    if guess_numbers[0] == guess_numbers[1] \
        or guess_numbers[0] == guess_numbers[2] \
        or guess_numbers[1] == guess_numbers[2]:
        print("같은 숫자를 입력하면 안 됩니다.")
        continue

    strike_count, ball_count = count_score(guess_numbers_tuple, numbers_tuple)

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", baseball_number_length - strike_count - ball_count)

    if strike_count == baseball_number_length:
        print("정답입니다.")
        break