# 접미사인지 확인하기
def solution(my_string, is_suffix):
    answer = 0
    answer = my_string.endswith(is_suffix)
    if answer == True:
        answer = 1
    else:
        answer = 0
    return answer