# 다음 소스 코드르 완성하여 1과 73 사이의 숫자 중
# 3으로 끝나는 숫자만 출력되게 만드세요.

i = 0
while True:
    i = i + 1
    if i % 10 != 3:
        continue

    if i > 73:
        break

    print(i)