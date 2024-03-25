# 대소문자 바꿔서 출력하기
str = input()

answer = ''
for i in str:
    if i.isupper():
        answer += i.lower()
    elif i.islower():
        answer += i.upper()
print(answer)