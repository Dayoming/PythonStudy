print("> 수비수가 고른 숫자")
number = [3, 2, 0]
print(number[0])
print(number[1])
print(number[2])

guess_number = []

while True:
    guess_number.clear()
    print("> 첫 번째 숫자를 입력하세요.")
    guess_number.append(int(input("prompt>")))
    print("> 두 번째 숫자를 입력하세요.")
    guess_number.append(int(input("prompt>")))
    print("> 세 번째 숫자를 입력하세요.")
    guess_number.append(int(input("prompt>")))

    print("> 공격수가 고른 숫자")
    print(guess_number[0])
    print(guess_number[1])
    print(guess_number[2])

    if guess_number[0] == guess_number[1] \
        or guess_number[0] == guess_number[2] \
        or guess_number[1] == guess_number[2]:
        print("같은 숫자를 입력하면 안 됩니다.")
        continue
    else:
        strike_count = 0
        ball_count = 0

    if guess_number[0] == number[0]:
        strike_count = strike_count + 1
    elif guess_number[0] == number[1] or guess_number[0] == number[2]:
        ball_count = ball_count + 1

    if guess_number[1] == number[1]:
        strike_count = strike_count + 1
    elif guess_number[1] == number[0] or guess_number[1] == number[2]:
        ball_count = ball_count + 1

    if guess_number[2] == number[2]:
        strike_count = strike_count + 1
    elif guess_number[2] == number[0] or guess_number[2] == number[1]:
        ball_count = ball_count + 1

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", 3 - strike_count - ball_count)

    if guess_number[0] == number[0] and guess_number[1] == number[1] and guess_number[2] == number[2]:
        print("정답입니다.")
        break