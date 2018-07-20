# 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 3과 5의 최소공배수인 15을 이용해 값을 구한다.