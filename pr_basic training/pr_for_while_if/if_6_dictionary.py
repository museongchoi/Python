# 수 조작하기
def solution(n, control):
    answer = 0
    cdic = {'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        n += cdic[i]
    answer = n
    return answer

# def solution(n, control):
#     answer = 0
#     for i in control:
#         if i == 'w':
#             n += 1
#         elif i == 's':
#             n -= 1
#         elif i == 'd':
#             n += 10
#         else:
#             n -= 10
#     answer = n
#     return answer