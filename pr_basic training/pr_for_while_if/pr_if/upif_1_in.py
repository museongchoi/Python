# 부분 문자열
def solution(str1, str2):
    answer = int(str1 in str2)
    return answer

# def solution(str1, str2):
#     answer = -1
#     answer = str2.find(str1)
#     if answer != -1:
#         answer = 1
#     else:
#         answer = 0
#     return answer