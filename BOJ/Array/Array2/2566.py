# 최댓값, 최대값의 idx를 출력
# arr 2차원 배열에 요소를 입력.
# maxnum으로 최대값 저장, 행을 순회하면서 최대값이 포함되어 있으면 해당 위치 출력.
arr = [[0 for _ in range(9)] for _ in range(9)]
maxnum = 0
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if maxnum < tmp[j]:
            maxnum = tmp[j]
        arr[i][j] = tmp[j]

print(maxnum)
for i in range(len(arr)):
    if maxnum in arr[i]:
        print(i+1, arr[i].index(maxnum)+1)

