count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world!', i)

# 반복문에서는 for i in range(count): 와 같이 range에 count를 넣어주면
# 입력받은 숫자만큼 반복된다.

for i in reversed(range(2, 11, 3)):
    print(i, end = ' ')