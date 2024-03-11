# 문자열 겹쳐 쓰기
def solution(my_string, overwrite_string, s):
    answer = ''
    len_over = len(overwrite_string)

    answer = my_string[0:s] + overwrite_string + my_string[s + len_over:]

    return answer