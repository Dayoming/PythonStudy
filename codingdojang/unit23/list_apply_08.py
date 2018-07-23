# 리스트에 map 함수 사용하기
# 튜플에서 map 함수를 사용할 수 있으며 원본 튜플을 변경하는 것이 아니라
# 새 튜플을 생성한다.

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])

print(a)

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

a = input().split()
print(a)
# input().split()의 결과가 리스트기 때문에 map을 사용할 수 있었다.

a = map(int, input().split())
print(a) # map 객체가 만들어짐

