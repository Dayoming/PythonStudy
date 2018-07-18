# 참(True)과 거짓(False)를 나타내는 불(Boolean)
print(1 == 1.0) # == 은 값을 비교한다
print(1 is 1.0) # is 는 객체를 비교한다(1은 정수 객체, 1.0은 실수 객체)

print(id(1))
print(id(1.0)) # 두 객체의 고유한 값이 다르다

print(bool(1))
print(bool(0))
print(bool('False'))
# 정수, 실수, 문자열을 불로 만들 때는 bool을 사용하면 된다.
# 이때 정수 1은 True, 0은 False
# 문자열의 값이 있으면 True, 없으면 False
