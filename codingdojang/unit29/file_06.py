# readlines : 한 줄씩 읽어서 리스트 형태로 가져오기

with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
