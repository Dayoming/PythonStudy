# set.union(세트1, 세트2)
# 두 세트의 합집합을 구한다. | 연산자와 같다.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(set.union(a, b))

# set.intersection(세트1, 세트2)
# 두 세트의 교집합을 구한다. & 연산자와 같다.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(set.intersection(a, b))

# set.difference(세트1, 세트2)
# 두 세트의 차집합을 구한다. - 연산자와 같다.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(set.difference(a, b))

# set.symmetric_difference(세트1, 세트2)
# 두 세트의 대상차집합을 구한다. ^ 연산자와 같다.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(set.symmetric_difference(a, b))

# update 계열 메서드는 a.update({5})와 같이 결과를 적용할 세트에서
# 메서드를 사용하면 된다. 할당 연산자와 같다.

a = {1, 2, 3, 4}
a.update({5})
print(a)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.intersection_update(b)
print(a)

a = {1, 2, 3, 4}
print(a.issubset({1, 2, 3, 4, 5}))
# 현재 세트가 다른 세트의 부분집합인지 확인

a = {1, 2, 3, 4}
print(a.issuperset({1, 2, 3}))
# 현재 세트가 다른 세트의 상위집합인지 확인

a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))
# 현재 세트가 다른 세트와 겹치지 않는지 확인

# len, add, remove, clear는 용법이 같다.

a = {1, 2, 3, 4}
a.discard(3)
print(a)
# 세트에서 특정 요소(값)을 삭제하고 요소가 없으면 그냥 넘어간다.

a = {1, 2, 3, 4}
a.pop()
print(a)
# 세트에서 임의의 요소(값)를 삭제하고 해당 요소를 반환한다.
# 만약 요소가 없으면 에러를 발생시킨다.