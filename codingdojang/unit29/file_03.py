# with as를 사용해서 자동으로 파일 객체 닫기
# with open(파일이름, 파일모드) as 파일객체:
#   코드

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)