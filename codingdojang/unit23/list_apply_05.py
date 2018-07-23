# 반복문으로 리스트의 요소를 모두 출력하기
a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

# for에서 인덱스를 지정하여 값을 가져오기
# i에 요소가 아닌 0부터 지정 리스트의 마지막 인덱스 값이 들어감
a = [38, 21, 53, 62, 19]
for i in range(len(a)):
    print(a[i])

# for에서 인덱스와 요소의 값을 동시에 출력하기
# enumerate 사용하면 반복문에서 인덱스와 요소의 값을 동시에 꺼내 올 수 있다.
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

# in 연산자는 리스트에 특정 값이 있는지 확인할 때도 사용할 수 있다.
a = [38, 21, 53, 62, 19]
print(21 in a) # True

a = [38, 21, 53, 62, 19]
print(21 not in a) # False

# While문으로 리스트 출력하기
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i = i + 1