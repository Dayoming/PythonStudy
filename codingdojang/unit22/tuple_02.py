a = (38, )
print(a) # 값 한 개짜리 튜플

a = ()
print(a) # 빈 튜플

a = tuple([1, 2, 3])
print(a) # 튜플에 리스트 넣기

b = tuple(range(10))
print(b)

c = tuple(range(5, 12))
print(c)

d = list(tuple(range(0, 10)))
print(d) # 리스트에 튜플을 넣어도 최종 결과는 리스트