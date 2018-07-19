if True:
    print('참')
else:
    print('거짓') # True는 참

if False:
    print('참')
else:
    print('거짓') # False는 거짓

if None:
    print('참')
else:
    print('거짓') # None은 거짓

if 0:
    print('참')
else:
    print('거짓') # 0은 거짓

if 1:
    print('참')
else:
    print('거짓') # 1은 참

# 숫자는 정수, 실수 관계없이 0은 거짓이고 0이 아닌 수는 참이다.
# 문자열은 비어있으면 거짓, 비어있지 않으면 참이다.

if not 0:
    print('참')

if not '':
    print('참')

if not None:
    print('참')

# 0, None, 빈 문자열을 뒤집으면 참이 되므로 if를 동작시킬 수 있다.
# 비어 있는 문자열, 리스트, 튜플, 딕셔너리, 세트도 False로 간주
# '', "", [ ], (), { }, set()
# 클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때도 False로 간주