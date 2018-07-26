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

# upate 계열 메서드는 a.update({5})와 같이 결과를 적용할 세트에서
# 메서드를 사용하면 된다. 할당 연산자와 같다.

a = {1, 2, 3, 4}
a.update({5})
print(a)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.intersection_update(b)
print(a)