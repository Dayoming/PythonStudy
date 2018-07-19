count = int(input('반복할 횟수를 입력하세요.: '))

for i in range(1, count + 1):
    if i % 2 != 0:
        continue
    print(i)