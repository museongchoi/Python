# 배열 만들기 3
def solution(arr, intervals):
    answer = []
    for x, y in intervals:
        answer.extend(arr[x:y+1])
    return answer