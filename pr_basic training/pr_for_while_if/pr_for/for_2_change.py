# 수열과 구간 쿼리3
def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]

    return arr