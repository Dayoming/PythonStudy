list = [1, 2, 3, 4, 5]

# ForEach문
# Java
# for(String str : list) {
#
# }
# Python
# for i in list:
#     print(i)

for i in range(len(list)):
    print(list[i])

for i in range(5, 10):
    print(i)
# 5~9

for i in range(5, 10, 2):
    print(i)
# 5, 7, 9

# range 함수 - 인자를 하나만 넣어주면 0부터 인자값의 미만까지 반환한다.
# len 함수 - size를 반환한다.