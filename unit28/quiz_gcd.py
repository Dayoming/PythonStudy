# math.gcd 함수 테스트

import math

num1, num2 = map(int, input().split())

divisor = set()

for i in range(1, math.gcd(num1, num2) + 1):
    if math.gcd(num1, num2) % i == 0:
        divisor.add(i)

print(divisor)

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)