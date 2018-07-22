# 코드 단축하기
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

# 문자열 곱셈을 이용하여 3의 배수일 때 'Fizz' 출력
# 문자열을 곱하면 문자열이 반복되고, 문자열을 더하면 두 문자열이 더해지는 특성 이용
# 특히 문자열에 True를 곱하면 문자열이 그대로 나오고, False를 곱하면 문자열이 출력되지 않는다.