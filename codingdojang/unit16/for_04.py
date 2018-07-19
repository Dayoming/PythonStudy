for i in range(10, 0, -1):
    print('Hello, world!', i)

# for i in range(10, 0)을 지정하면 숫자가 감소하지 않음
# range는 숫자가 증가하는 기본 값이 양수 1이기 때문
# 증가 폭을 음수로 지정하면 숫자 역순 생성 가능

for i in reversed(range(10)):
    print('Hi, world!', i)

# reversed를 사용하면 숫자의 순서를 반대로 뒤집을 수 있다.

for i in reversed(range(10, 0, -2)):
    print('Hellow, world!', i)