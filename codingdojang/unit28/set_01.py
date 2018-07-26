# 집합을 표현하는 세트(set)라는 자료형 제공
# 합집합, 교집합, 차집합 등의 연산이 가능

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)
# [ ] 로 특정 요소만 출력할 수 없음

a = set('apple')
print(a) # 중복된 문자는 포함되지 않는다.

b = set(range(5))
print(b)

c = set()
print(type(c))
# 빈 set 만들기
# 세트가 { } 를 사용한다고 해서 c = { }와 같이 만들면
# 빈 딕셔너리가 만들어지므로 주의!

# 세트 안에서 세트 사용 불가능

a = frozenset(range(10))
print(a)
# 내용을 변경할 수 없는 세트도 제공