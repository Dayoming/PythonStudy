# 표준 입력으로 숫자 두 개가 입력됩니다.
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
# 그리고 세트 변수는 divisor를 사용하세요.
# 단, 최종 결과는 공약수의 합으로 판단합니다.

def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b
# 유클리드 호제법
# 최대공약수를 구하는 함수를 gcd(a, b)라고 하자.
# a mod b = 0 이라면, gcd(a, b) = b 임이 성립.
# a mod b != 0 이라면, gcd(a, b) = gcd(b, a mod b) 임이 성립한다.

num1, num2 = map(int, input().split())

divisor = set()

for i in range(1, gcd(num1, num2) + 1):
    if gcd(num1, num2) % i == 0:
        divisor.add(i)


result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)