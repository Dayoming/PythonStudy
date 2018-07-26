# 파일 객체는 이터레이터기 때문에 for 반복문에 바로 사용 가능

file = open('hello.txt', 'r')
for line in file:
    print(line.strip('\n'))

# 이터레이터라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능
file = open('hello.txt', 'r')
a, b, c = file
print(a, b, c)