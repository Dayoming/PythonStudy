i = 1
while i <= 100:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

# while 문에서도 동작은 같다.
# 여기서는 반복 횟수를 정한 뒤 continue를 사용했지만 무한 루프에서
# continue를 사용하면 짝수만 계속 출력될 뿐 반복문은 끝나지 않음