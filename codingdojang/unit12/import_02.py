import math as m
# import 모듈 as 새이름

print(m.sqrt(4.0))
# 단, 모듈의 새 이름은 현재 파이썬 셸이나 스크립트 파일 안에서만 유효

import urllib.request as r

response = r.urlopen("http://www.google.co.kr")
print(response.status)