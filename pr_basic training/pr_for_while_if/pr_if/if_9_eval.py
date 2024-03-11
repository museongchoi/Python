# 조건 문자열
def solution(ineq, eq, n, m):
    answer = 0
    answer = int(eval(str(n)+ineq+eq.replace('!', "")+str(m)))
    return answer