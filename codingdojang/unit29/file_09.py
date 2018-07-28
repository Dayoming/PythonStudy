# 파이썬 객체를 파일에 저장하기, 가져오기
import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathmatics': 85, 'science': 82}

# hello.txt 파일을 바이너리 쓰기 모드(wb)로 열기
# 읽기 모드는 rb
with open('james.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
