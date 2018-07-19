# for에서도 break의 동작은 같다.

for i in range(0, 10000):
    print(i)
    if i == 100:
        break