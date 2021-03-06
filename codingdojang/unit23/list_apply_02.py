a = [10, 20, 30, 10, 25, 40]
print(a.count(10))
# 리스트에서 특정 값의 개수를 구한다.

a = [10, 20, 30, 10, 25, 40]
print(a.index(20))
# 특정 값의 인덱스를 구한다.

a = [10, 20, 30, 10, 25, 40]
a.reverse()
print(a)
# 리스트에서 값의 순서를 반대로 뒤집는다.

a = [10, 20, 30, 10, 25, 40]
a.sort()
print(a)
# 리스트의 값을 작은 순서대로 정렬(오름차순)

a.clear()
print(a)
# 모든 값을 삭제한다.

a = [1, 2, 3]
a[len(a):] = [10]
print(a)
# 인덱스로 범위를 지정하여 조작 가능
# a[len(a):] 는 시작 인덱스를 len(a)로 지정해서 리스트의 마지막 인덱스보다 1 큰 상태
# 리스트의 맨 뒤부터 시작하겠다는 뜻
# append와 같다.

a = [1, 2, 3]
a[len(a):] = [10, 20]
print(a)
# 리스트를 할당하면 extend와 같다.

a = [10, 20, 30, 40, 50]
del a[1]
print(a)
# 리스트의 값을 삭제할 때는 del a[1]과 같이 del을 사용하여 특정 인덱스의 값을 삭제
# a.pop(1)과 같다.

a = [10, 20, 30, 40, 50]
del a[1:4]
print(a)
# 시작 인덱스와 끝 인덱스를 지정하면 시작 인덱스와 끝 인덱스 직전까지 삭제

a = [10, 20, 30, 40, 50]
del a[:]
print(a)
# 지정하지 않으면 a.clear()와 같음
