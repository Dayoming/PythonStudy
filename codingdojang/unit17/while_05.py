import random

i = 0
while i != 3:
    i = random.randint(0, 9)
    print(i)

# i 가 3이 아닐때 계속 반복
# 0부터 9까지 무작위로 생성
# 정수가 무작위로 생성되므로 실행할 때마다 반복 횟수가 달라짐
# while 반복문은 반복 횟수가 정해져 있지 않을 때 유용