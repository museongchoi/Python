# 기능 개발
def solution(progresses, speeds):
    answer = []
    my_list = []
    # pro 남은 프로세스 저장
    # 해당 프로세스의 speeds 저장
    # pro % spe 나머지가 0이면 몫을 저장, 나머지가 0이 아니면 한번 더 실행 몫 + 1
    for idx, i in enumerate(progresses):
        pro = 100 - i
        spe = speeds[idx]
        if pro % spe == 0:
            my_list.append(pro // spe)
        else:
            my_list.append((pro // spe) + 1)

    # idx 0 번째 저장 1번부터 비교
    # 앞 프로세스가 진행되는 동안 뒤 프로세스는 진행이 불가
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