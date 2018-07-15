print("> 수비수가 고른 숫자")
number1 = 3
number2 = 2
number3 = 0
number = [number1, number2, number3]
print(number1)
print(number2)
print(number3)

print("> 첫 번째 숫자를 입력하세요.")
guess_number1 = int(input("prompt>"))
print("> 두 번째 숫자를 입력하세요.")
guess_number2 = int(input("prompt>"))
print("> 세 번째 숫자를 입력하세요.")
guess_number3 = int(input("prompt>"))

guess_number = [guess_number1, guess_number2, guess_number3]

print("> 공격수가 고른 숫자")
print(guess_number1)
print(guess_number2)
print(guess_number3)

if guess_number[0] == guess_number[1] \
    or guess_number[0] == guess_number[2] \
    or guess_number[1] == guess_number[2]:
    print("같은 숫자를 입력하면 안 됩니다.")
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


# for i in range(len(guess_number)):
#     if number[i] == guess_number[i]:
#         strike_count += 1
#     elif number[i] == guess_number[i+1]:
#         ball_count += 1
#     elif number[i] == guess_number[i+2]:
#         ball_count += 1

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", 3 - strike_count - ball_count)
