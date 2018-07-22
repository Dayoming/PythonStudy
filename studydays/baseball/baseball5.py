from random import *

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

guess_numbers = [3, 2, 0]
input_message = ["> 첫 번째 숫자를 입력하세요.", "> 두 번째 숫자를 입력하세요.", "> 세 번째 숫자를 입력하세요."]

while True:
    guess_numbers.clear()

    for i in range(baseball_number_length):
        print(input_message[i])
        guess_numbers.append(int(input("prompt> ")))

    print("> 공격수가 고른 숫자")

    for i in range(baseball_number_length):
        print(guess_numbers[i])

    if guess_numbers[0] == guess_numbers[1] \
        or guess_numbers[0] == guess_numbers[2] \
        or guess_numbers[1] == guess_numbers[2]:
        print("같은 숫자를 입력하면 안 됩니다.")
        continue

    strike_count = 0
    ball_count = 0

    for i in range(baseball_number_length): # 0, 1, 2 세번
        for j in range(baseball_number_length): # 0, 1, 2 세번
            if guess_numbers[i] == numbers[j]: # ball 조건
                if i == j: # strike 조건
                    strike_count = strike_count + 1
                else:
                    ball_count = ball_count + 1

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", baseball_number_length - strike_count - ball_count)

    if strike_count == baseball_number_length:
        print("정답입니다.")
        break