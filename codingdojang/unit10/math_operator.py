print(5/2)
print(5//2)
# 5//2와 같이 //로 나누면 2가 나온다.
# 즉, //은 결과에서 소수점 이하는 버린다.

print(5%2)
print(2**10)
# 나머지를 구하는 모듈로(modulo) 연산자
# 거듭제곱을 구하는 ** 연산자

print(divmod(5, 2))
# 몫과 나머지를 함께 구하는 divmod

quotient, remainder = divmod(5, 2)
print(quotient, remainder)
# divmod는 몫과 나머지를 튜플로 반환한다.

x = -10
print(+x)
print(-x)
# 값이나 변수 앞에 양수, 음수 부호를 붙인다.