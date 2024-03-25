# 수 조작하기 2
def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        tmp = numLog[i] - numLog[i-1]
        if tmp == 1:
            answer += 'w'
        elif tmp == -1:
            answer += 's'
        elif tmp == 10:
            answer += 'd'
        elif tmp == -10:
            answer += 'a'
    return answer