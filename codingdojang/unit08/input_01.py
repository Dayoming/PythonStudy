# input 한 번에 값을 여러 개 입력받으려면?
# input에서 split을 사용한 뒤 여러 개의 변수에 저장해주면 된다(각 변수는 콤마로 구분)

# 변수1, 변수2 = input().split()
# 변수1, 변수2 = input().split(기준문자)
# 변수1, 변수2 = input(문자열).split()
# 변수1, 변수2 = input(문자열).split(기준문자)

a, b = input('문자열 두 개를 입력하세요: ').split()

print(a)
print(b)
# 입력받은 값을 공백을 기준으로 분리하여 변수에 차례로 저장

a, b = map(int, input('숫자 두 개를 입력하세요: ').split())

print(a + b)
# map 함수를 사용하면 받은 값을 해당 자료형으로 변환해줌

a, b = map(int, input('숫자 두 개를 입력하세요: ').split(','))

print(a + b)