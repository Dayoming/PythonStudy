print(1, 2, 3)
print('Hello', 'Python')
# print 에는 변수나 값 여러 개를 ,(콤마)로 구분하여 넣을 수 있다.
# 공백으로 띄워져서 한 줄로 출력된다.

print(1, 2, 3, sep=', ')
print(4, 5, 6, sep=',')
print('Hello', 'Python', sep='')
print(1920, 1080, sep='x')
# 값 사이에 공백이 아닌 다른 문자를 넣고 싶으면 sep(separator)에 문자 또는 문자열 지정