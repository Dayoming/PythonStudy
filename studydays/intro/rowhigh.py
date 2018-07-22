from random import *

random_num = randrange(1, 101)
print(random_num)

while True:
    print("숫자를 입력해주세요.")
    input_num = input("prompt> ")

    input_num = int(input_num)

    if random_num != input_num:
        if random_num > input_num:
            print("입력한 수보다 큽니다.")
            continue
        elif random_num < input_num:
            print("입력한 수보다 작습니다.")
            continue
    else:
        print("정답입니다! 프로그램을 종료합니다.")
        break