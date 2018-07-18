from math import pi
print(pi)
# 원하는 변수만 가져오기

from math import sqrt
print(sqrt(20))
# 원하는 함수만 가져오기

from math import *
print(pi)
# math 모듈의 변수, 함수, 클래스를 가져온다.

from urllib.request import Request, urlopen
# urlopen 함수, Request 클래스를 가져옴

req = Request('http://www.google.co.kr')
response = urlopen(req)
print(response.status)

# import로 가져온 모듈(변수, 함수, 클래스)은 del로 해제할 수 있습니다.
# 모듈을 다시 가져오려면 importlib.reload를 사용합니다.