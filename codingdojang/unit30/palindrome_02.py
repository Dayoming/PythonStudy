# 회문 판별 과정
text = 'Hello'
for i in range(len(text) - 1): # 2-gram이므로 문자열의 끝에서 한 글자 앞까지
    print(text[i], text[i + 1], sep='') # 현재 문자와 그다음 문자 출력