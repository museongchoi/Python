# 정수 찾기
def solution(num_list, n):
    answer = 0
    cnt = num_list.count(n)
    if cnt != 0:
        answer = 1
    return answer