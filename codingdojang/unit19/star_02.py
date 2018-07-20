# 사각형으로 별 출력하기

for i in range(5):
    for j in range(5):
        print('*', end='') # 별 출력. end에 ''를 지정하여 줄바꿈X
    print() # print는 출력 후 기본적으로 다음 줄로 넘어감

print()

for i in range(3):
    for j in range(7):
        print('*', end='')
    print()