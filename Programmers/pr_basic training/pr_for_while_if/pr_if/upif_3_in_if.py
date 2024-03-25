# 배열의 원소 삭제하기

def solution(arr, delete_list):
    answer = [x for x in arr if x not in delete_list]
    return answer

# def solution(arr, delete_list):
#     answer = []
#
#     for i in arr:
#         bol = False
#         for j in delete_list:
#             if i == j:
#                 bol = True
#         if bol == False:
#             answer.append(i)
#     return answer