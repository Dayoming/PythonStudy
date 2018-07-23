# 리스트 표현식 사용하기
# 리스트 컴프리헨션(list comprehension)
# 리스트 안에 식, for 반복문 등을 지정하여 리스트를 생성하는 것
# 리스트 내포, 리스트 내장, 리스트 축약, 리스트 해석

# [ 식 for 변수 in 리스트 ]
# list(식 for 변수 in 리스트)

a = [i for i in range(10)] # 0부터 9까지 숫자를 생성하여 리스트 생성
print(a)

b = list(i for i in range(10))
print(b)

# range(10) -> 숫자 10개 생성
# for i -> 숫자를 하나씩 꺼냄
# i로 리스트 생성 순으로 진행

# 식 부분에서 i를 다른 값과 연산하면 각 연산의 결과를 리스트로 생성
c = [i + 5 for i in range(10)]
print(c)

# [ 식 for 변수 in 리스트 if 조건식 ]
# list(식 for 변수 in 리스트 if 조건식)
a = [i for i in range(10) if i % 2 == 0]
print(a) # 0~9 숫자 중 2의 배수인 숫자로 리스트 생성

b = [i + 5 for i in range(10) if i % 2 == 1]
print(b) # 0~9 숫자 중 홀수인 수에 5을 더한 리스트 생성

# range(10) -> if문 -> for i -> i + 5

a = [i * j for j in range(2, 10)
           for i in range(1, 10)]
print(a)
# for가 여러 번 있을 때 처리 순서는 뒤에서 앞으로 순
