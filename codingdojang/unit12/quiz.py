# 표준 입력으로 원의 반지름(실수)이 입력됩니다.
# 입력된 반지름을 이용하여 원의 넓이를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 원의 넓이는 반지름 * 반지름 * 원주율로 구합니다.

from math import pi

radius = float(input())

print(radius * radius * pi)