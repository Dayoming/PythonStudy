# 문자열 여러 줄에 파일에 쓰기, 읽기

with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

# 파일에 문자열 여러 줄을 저장할 때 주의할 부분은 개행 문자 부분
# 'Hello, world! {0}\n' 와 같이 문자열 끝에 개행 문자 \n 를 지정해주어야 줄바꿈이 됨