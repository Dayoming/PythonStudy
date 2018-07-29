# 회문 판별하기
# 회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장
word = input('단어를 입력하세요.')

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        is_palindrome = False
        break

print(is_palindrome)