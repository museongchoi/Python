# 원소들의 곱과 합
def solution(num_list):
    answer = 0
    pro = 1
    tot = 0
    for num in num_list:
        pro *= num
        tot += num

    if pro > tot ** 2:
        answer = 0
    else:
        answer = 1

    return answer