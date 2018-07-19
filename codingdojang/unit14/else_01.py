# if, else에서 변수에 값을 할당할 때는
# 변수 = 값 if 조건문 else 값 형식으로 축약 가능
# 이런 문법을 조건부 표현식이라고 부른다.
# 보통 람다 표현식에서 사용

x = 5
y = x if x == 10 else 0
print(y)

x = 5
if x == 10:
    y = x
else:
    y = 0
print(y)

# 위 표현식과 아래 조건문은 같다.