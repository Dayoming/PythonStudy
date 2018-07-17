# 파이썬은 값 자체도 객체이다.
# 그래서 변수에 값을 그대로 저장하지 않고 객체를 가리키는 방식을 사용한다.
# (C언어처럼 오래 전에 나온 언어는 변수에 값을 그대로 저장)

# 예를 들어 다음과 같이 x와 y에 1000을 할당했다면 x와 y는 단지 1000이라는 객체를 가리킬 뿐
# x = 1000
# y = 1000

import sys
print(sys.getrefcount(1000))
# sys.getrefcount 함수를 사용하면 현재 객체가 몇 번 사용되었는지 확인할 수 있음
# 객체를 사용(참조)한 횟수를 레퍼런스 카운트(reference count)라고 부른다.

x = 1000
print(sys.getrefcount(1000))

y = 1000
print(sys.getrefcount(1000))

print(x is y)
# 객체가 같은지 판단하는 연산자 is
# 같은 객체를 가리키고 있다.