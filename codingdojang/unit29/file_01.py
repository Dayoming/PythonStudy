# 파일에 문자열 쓰기, 읽기

# 파일객체 = open(파일이름, 파일모드)
# 파일객체.write(문자열)
# 파일객체.close()

file = open('hello.txt', 'w')
# hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
print(type(file))

file.write('Hello, world!')
file.close()

# open 함수로 파일을 열어서 파일 객체 얻기
# 파일 이름을 지정하고 파일 모드를 쓰기로 지정해주기
# write로 파일에 문자열 쓰기
# 파일 쓰기가 끝나면 반드시 close로 파일 객체 닫아주기