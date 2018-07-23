# 리스트의 가장 작은 수, 가장 큰 수, 합계 구하기
# 가장 작은 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i

print(smallest)

# 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i

print(largest)

# 정렬함수를 이용해서 가장 큰 수 구하기
# 정렬은 기본적으로 오름차순
# smallest, largest = a[0], a[-1]
a = [38, 21, 53, 62, 19]
a.sort()
print(a[0])

a.sort(reverse=True)
print(a[0])

# min, max 함수 이용해서 구하기
a = [38, 21, 53, 62, 19]
print(min(a))
print(max(a))

# 리스트의 요소 합계 구하기
a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x = x + i

print(x)

# sum 함수를 이용해서 구하기
a = [10, 10, 10, 10, 10]
print(sum(a))