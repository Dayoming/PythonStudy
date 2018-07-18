# 파이썬은 표준 라이브러리 이외에도 파이썬 패키지 인덱스를 통해 다양한 패키지 사용 가능
# 특히 명령만 입력하면 원하는 패키지를 인터넷에서 다운로드하여 설치해줄 뿐만 아니라
# 관련된 패키지(의존성)까지 설치해주므로 매우 편리!
# pip은 파이썬 패키지 인덱스의 패키지 관리 명령어이며 Windows용 파이썬에는 기본적으로 내장

# pip install 설치할 패키지명

import requests

r = requests.get('http://www.google.co.kr')
print(r.status_code)

# 패키지 검색 : pip search 패키지
# 특정 버전의 패키지를 설치 : pip install 패키지==버전
# 패키지 목록 출력 : pip list 또는 pip freeze
# 패키지 삭제 : pip uninstall 패키지