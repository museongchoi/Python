# 특별한 2차원 배열
def solution(arr):
    answer = 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                answer = 0
    return answer