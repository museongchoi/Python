# 등차 수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0
    keys = list(range(a, a + d * len(included), d))
    tmp = dict(zip(keys, included))

    for i in tmp:
        if tmp.get(i) == True:
            answer += i
    return answer