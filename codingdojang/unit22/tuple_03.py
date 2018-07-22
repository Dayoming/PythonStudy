# 리스트와 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있다.
# 이때 변수읙 개수와 리스트(튜플)의 요소 개수는 같아야 한다.

a, b, c = [1, 2, 3]
print(a, b, c)

d, e, f = (1, 2, 3)
print(d, e, f)

# 리스트와 튜플 변수로도 변수 여러 개를 만들 수 있다.
# 다음과 같이 리스트와 튜플의 요소를 변수 여러 개에 할당하는 것을
# 리스트 언패킹(list unpacking), 튜플 언패킹(tuple unpacking)이라고 한다.

x = [1, 2, 3] # 리스트 패킹
a, b, c = x # 리스트 언패킹
print(a, b, c)

y = (4, 5, 6) # 튜플 패킹
d, e, f = y # 튜플 언패킹
print(d, e, f)