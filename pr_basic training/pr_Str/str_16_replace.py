# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    answer = ''
    answer = my_string.replace(alp, alp.upper())

    return answer