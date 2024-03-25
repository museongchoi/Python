# 홀수 vs 짝수
def solution(num_list):
    answer = 0
    num1 = sum(num_list[0::2])
    num2 = sum(num_list[1::2])

    answer = max(num1, num2)
    return answer