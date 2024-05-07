# 서울 지하철 2호선

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def DFS(x, st_i, cnt):
    global ans
    if ans:
        return

    visited[x] = True
    for k in arr[x]:
        if visited[k] == False:
            DFS(k, st_i, cnt + 1)
            if not ans:
                visited[k] = False
        elif visited[k] == True and k == st_i and cnt >= 3:
            ans = True
            return

n = int(input())
arr = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = False
count = [0 for _ in range(n)]

for _ in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,n+1):
    if visited[i] == False:
        DFS(i, i, 1)
        if ans == True:
            break

from collections import deque
def BFS(j):
    visited[j] = True
    dq = deque()
    dq.append([j, 0])

    while dq:
        xx, cnt = dq.popleft()
        for k in arr[xx]:
            if visited[k] == True:
                # j : 처음 값을 인덱스로 사용하여 거리를 저장한다.
                count[j-1] = count[k-1] + 1
                break
            elif visited[k] == False:
                dq.append([k, cnt+1])

for j in range(1, n+1):
    if visited[j] == False:
        BFS(j)
    print(count[j-1], end=' ')

