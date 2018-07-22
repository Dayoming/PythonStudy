
print('> 게임이 시작합니다.')

order = {'청기 올려': 'R', '청기 내려': 'F',
         '백기 올려': 'U', '백기 내려': 'J'}
# dictionary
# '청기 올려' -> key
# 'R' -> value

# 문자열은 상수다.

while True:
    button = 'R'
    input_char = input('> ')

    if button == input_char.upper():
        print('성공!')
    else:
        print('실패!')
        break
