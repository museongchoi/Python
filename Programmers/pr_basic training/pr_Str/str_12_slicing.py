# 배열 만들기 5
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        el = int(i[s:s+l])
        print(el)
        if k < el:
            answer.append(el)
    return answer