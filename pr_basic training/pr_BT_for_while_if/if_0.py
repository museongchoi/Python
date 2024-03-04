# 이어 붙인 수
def solution(num_list):
    answer = 0
    sum1 = ''
    sum2 = ''
    for i in num_list:
        if i%2 == 0:
            sum1 += str(i)
        else:
            sum2 += str(i)
    answer = int(sum1) + int(sum2)
    return answer