# 함수, 튜플, 딕셔너리를 사용해 숫자야구 게임 만들기
from random import *

def print_message(num):
    input_number = {0: "> 첫 번째 숫자를 입력하세요.",
                    1: "> 두 번째 숫자를 입력하세요.",
                    2: "> 세 번째 숫자를 입력하세요."}

    print(input_number[num])

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
        print(guess_numbers_tuple[i])

    guess_number1, guess_number2, guess_number3 = guess_numbers_tuple

    if guess_number1 == guess_number2 \
        or guess_number1 == guess_number3 \
        or guess_number2 == guess_number3:
        print("같은 숫자를 입력하면 안 됩니다.")
        continue

    strike_count = 0
    ball_count = 0

    for i in range(baseball_number_length):
        if guess_numbers[i] == numbers[i]:
            strike_count = strike_count + 1
        elif guess_numbers[i] in numbers:
            ball_count = ball_count + 1

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", baseball_number_length - strike_count - ball_count)

    if strike_count == baseball_number_length:
        print("정답입니다.")
        break