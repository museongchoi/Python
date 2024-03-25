# 첫 번째로 나오는 음수
def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i

    answer = -1
    return answer