# 파일의 내용을 한 줄씩 순차적으로 읽으려면?
# 변수 = 파일객체.readline()

with open('hello.txt', 'r') as file:
    line = file.readline()
    print(line.strip('\n'))
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

# 문자열을 출력할 때 stript('\n')과 같이 \n을 삭제한 이유?
# 문자열 안에 든 \n과 print가 출력하는 \n 때문에 줄바꿈이 두 번 일어나기 때문