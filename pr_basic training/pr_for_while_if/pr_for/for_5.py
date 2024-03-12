# 배열 만들기 2
def solution(l, r):
    answer = []
    st = ''
    for i in range(l, r + 1):
        if i % 5 == 0:
            bo = False
            st = str(i)
            for stidx in range(len(st)):
                if st[stidx] != '0' and st[stidx] != '5':
                    bo = True
            if bo == False:
                answer.append(i)

    if not answer:
        answer.append(-1)
    return answer