list = [1, 2, 3, 4, 5]

list[2] = 8

print(list)
print(list[2])
print(list[4])

list.append(99)
# 리스트에 추가하기
print(list)

pop = list.pop()
# 리스트의 맨 마지막 항목을 반환한다
list.pop()
# 리스트의 맨 마지막 항목이 사라진다
print(list)