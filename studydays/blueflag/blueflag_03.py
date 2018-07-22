from random import *

print('> 게임이 시작합니다.')

order = {'청기 올려': 'R', '청기 내려': 'F',
         '백기 올려': 'U', '백기 내려': 'J'}
# dictionary
# '청기 올려' -> key
# 'R' -> value

# q 추가
# count 추가

order_message = list(order.keys())
count = 0

while True:
    random_index = randrange(len(order_message))
    message = order_message[random_index]

    print('>', message)
    button = order[message]

    input_char = input('> ')

    if button == input_char.upper():
        print('성공!')
        count = count + 1
    elif input_char == 'q' or input_char == 'Q':
        print(str(count) + '번 맞추셨습니다.')
        break
    else:
        print('실패!')
        print(str(count) + '번 맞추셨습니다.')
        break
