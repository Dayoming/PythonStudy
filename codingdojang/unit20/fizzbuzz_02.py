# 3의 배수일 때와 5의 배수일 때 처리하기

for i in range(1, 101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)