# 모듈 : 특정 기능을 .py 파일 단위로 작성한 것
# 패키지 : 특정 기능과 관련된 여러 모듈을 묶은 것. 보통 인터넷에 있는 패키지를 설치해서 사용
# 라이브러리 : 파이썬에 기본적으로 설치된 모듈과 내장 함수를 묶어서 파이썬 표준 라이브러리(Python Standard Library, PSL)라 부름

import math
print(math.pi) # 원주율
print(math.sqrt(2.0)) # 제곱근

# import는 패키지의 모듈도 가져올 수 있다.
import urllib.request
response = urllib.request.urlopen("http://www.google.co.kr")
print(response.status)

# 패키지.모듈 형식으로 가져오며, 모듈의 함수를 사용할 때도 패키지.모듈.함수() 형식으로 가져옴
# urllib.request.urlopen은 URL을 여는 함수
# URL 열기에 성공하면 response.status의 값이 200이 나온다. (HTTP 상태 코드)