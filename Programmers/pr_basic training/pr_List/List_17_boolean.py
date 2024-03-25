# 할 일 목록
def solution(todo_list, finished):
    answer = []
    for idx, i in enumerate(todo_list):
        if finished[idx] == False:
            answer.append(i)
    return answer