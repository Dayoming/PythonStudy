# 반복문으로 2차원 리스트의 요소를 출력하기
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y)
# 안쪽 리스트에서 값 두 개를 꺼내서 x, y에 넣는다.

a = [[10, 20], [30, 40], [50, 60]]
for i in a: # 안쪽 리스트를 꺼냄
    for j in i: # 안쪽 리스트에서 값을 하나씩 꺼냄
        print(j, end=' ')
    print()

a = [[10, 20], [30, 40], [50, 60]]
for i in range(len(a)): # 세로 크기
    for j in range(len(a[i])): # 가로 크기
        print(a[i][j], end=' ')
    print()

a = [[10, 20], [30, 40], [50, 60]]
i = 0
while i < len(a): # 반복할 때 리스트의 크기 활용(세로 크기)
    x, y = a[i] # x, y에 [10, 20] 등 할당
    print(x, y)
    i = i + 1 # 인덱스를 1 증가시킴

