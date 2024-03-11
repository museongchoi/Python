# 배열 만들기 2
def solution(l, r):
    answer = []
    bo = False
    for i in range(l, r + 1):
        if i % 5 == 0:
            st = str(i)
            for stidx in range(len(st)):
                if str[stidx] != '0' and str[stidx] != '5':
                    bo = True
                    break
            if bo == False:
                answer.append[i]

    if not answer:
        answer.append(-1)
    return answer