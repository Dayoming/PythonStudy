# 문자열에 + 를 사용하면 문자열이 연결되고, * 를 사용하면 문자열이 반복됨
# 문자열1 + 문자열2
# 문자열 * 정수

hello = 'Hello, '
world = 'world!'
print(hello + world)

print(hello * 3)
# 0 또는 음수를 곱하면 빈 문자열이 나오며 실수는 곱할 수 없다.

print(hello + str(10))
# 문자열에 정수를 더하려고 하면 에러가 발생
# 이때는 str를 사용하여 숫자(정수, 실수)를 문자열로 변환하면 됨

