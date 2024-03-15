# 같은 숫자는 싫어
def solution(arr):
    answer = []

    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        elif answer[-1] == i:
            continue
        else:
            answer.append(i)
    return answer


def solution(arr):
    answer = []
    print(range(1, len(arr)))
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer