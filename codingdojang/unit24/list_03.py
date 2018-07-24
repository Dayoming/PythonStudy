# 반복문으로 2차원 리스트 만들기
a = []
for i in range(3):
    line = [] # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0) # 안쪽 리스트에 0 추가
    a.append(line) # 전체 리스트에 안쪽 리스트 추가

print(a)

# 리스트 표현식을 이용해 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)