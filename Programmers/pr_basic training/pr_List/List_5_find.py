# 원하는 문자열 찾기
def solution(myString, pat):
    answer = 0
    idx = -1
    myString = myString.upper()
    pat = pat.upper()
    idx = myString.find(pat)

    if idx != -1:
        answer = 1
    return answer