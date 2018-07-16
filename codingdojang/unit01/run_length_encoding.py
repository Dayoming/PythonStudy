
data = 'aaaaabbbccccccddddddddd'
encoded = ''

count = 1
for i in range(1, len(data)): # 1부터 data의 길이(23 - 1)까지
    if data[i] == data[i - 1]: # data의 글자가 이전 글자와 같으면
        count += 1 # count + 1
    else: # 아니면
        encoded += data[i - 1] + str(count) # encoded에 data의 이전 글자와 count를 저장한다
        count = 1 # count를 초기화한다

    if i == len(data) - 1: # i가 data의 길이와 같으면
        encoded += data[i] + str(count) # encoded에 data의 글자와 count를 저장한다

print(encoded)

# a5b3c6d9 Run-Length Ecdoing, PCX 그림 파일 포맷에 쓰임
# 이처럼 문제에서 일정한 패턴을 발견하고, 패턴을 토대로 문제를 해결하는 절차가 알고리즘이다.
