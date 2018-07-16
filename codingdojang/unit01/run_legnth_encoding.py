
data = 'aaaaabbbccccccddddddddd'
encoded = ''

count = 1
for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        count += 1
    else:
        encoded += data[i - 1] + str(count)
        count = 1

    if i == len(data) - 1:
        encoded += data[i] + str(count)

print(encoded)
# a5b3c6d9 Run-Length Ecdoing, PCX 그림 파일 포맷에 쓰임
# 이처럼 문제에서 일정한 패턴을 발견하고, 패턴을 토대로 문제를 해결하는 절차가 알고리즘이다.
