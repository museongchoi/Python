# 기능 개발
def solution(progresses, speeds):
    answer = []
    my_list = []

    for idx, i in enumerate(progresses):
        pro = 100 - i
        spe = speeds[idx]
        if pro % spe == 0:
            my_list.append(pro // spe)
        else:
            my_list.append((pro // spe) + 1)

    cnt = 1
    tmp = my_list[0]

    for j in my_list[1:]:
        if tmp >= j:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            tmp = j

    answer.append(cnt)

    return answer