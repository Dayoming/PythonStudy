# hello.txt 파일의 문자열 읽기

file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()

# open을 사용하여 읽기 모드로 객체 반환
# read의 반환값을 변수에 저장해주고 출력
# close로 파일 객체 닫아주기