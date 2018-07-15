# 첫 번째 숫자 입력 받으세요.
# 두 번째 숫자 입력 받으세요.
# 연산자 + - * / 입력 받으세요.

number1 = input("첫 번째 숫자 입력 받으세요.")
number2 = input("두 번째 숫자 입력 받으세요.")
operator = input("연산자 + - * / 입력 받으세요.")

number1 = int(number1)
number2 = int(number2)

# 파이썬에서 들여쓰기는 문법이다!
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
else:
    print((number1 / number2))