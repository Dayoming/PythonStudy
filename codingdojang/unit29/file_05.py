# 리스트에 들어있는 문자열 파일에 저장
# writelines를 사용

lines = {'hello.\n', 'python\n', 'programming.\n'}

with open('hello.txt', 'w') as file:
    file.writelines(lines)