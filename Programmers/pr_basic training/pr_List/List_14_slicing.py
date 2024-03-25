# 5명씩
def solution(names):
    answer = []
    for i in names[::5]:
        answer.append(i)
    return answer