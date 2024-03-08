# 소문자로 바꾸기
def solution(myString):
    answer = ''
    for i in myString:
        if i.isupper() == True:
            answer += i.lower()
        else:
            answer += i
    return answer