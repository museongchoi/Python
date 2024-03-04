# 더 크게 합치기
def solution(a, b):
    answer = 0
    tmp1 = str(a) + str(b)
    tmp2 = str(b) + str(a)
    answer = max(int(tmp1), int(tmp2))
    return answer