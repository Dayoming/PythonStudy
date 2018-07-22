from random import *

print('> 게임이 시작합니다.')

order = {'청기 올려': 'R', '청기 내려': 'F',
         '백기 올려': 'U', '백기 내려': 'J'}
# dictionary
# '청기 올려' -> key
# 'R' -> value

# 문자열은 상수다.

order_message = list(order.keys())

while True:
    random_index = randrange(len(order_message))
    message = order_message[random_index]

    print('>', message)
    button = order[message]

    input_char = input('> ')

    if button == input_char.upper():
        print('성공!')
    else:
        print('실패!')
        break
