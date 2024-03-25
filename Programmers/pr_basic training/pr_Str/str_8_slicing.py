# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        answer += my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer