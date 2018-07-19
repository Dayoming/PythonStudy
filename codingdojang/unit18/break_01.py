# break는 for, while 문법에서 제어 흐름을 벗어나기 위해 사용
# 루프를 완전히 중단
# countinue는 제어흐름(반복)을 유지한 상태에서 코드의 실행만 건너뜀

i = 0
while True:
    i += 1
    print(i)
    if i == 100:
        break
# 숫자를 증가시키다가 100이 나오면 반복문 종료