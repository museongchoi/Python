# 순서 바꾸기
def solution(num_list, n):
    answer = []
    answer = num_list[n:]
    for i in num_list[:n]:
        answer.append(i)

    return answer
def solution(num_list, n):
    answer = []
    answer.extend(num_list[n:] + num_list[:n])
    return answer