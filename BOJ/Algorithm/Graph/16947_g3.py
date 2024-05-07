# 서울 지하철 2호선

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def DFS(x, st_i, cnt):
    global ans
    if ans:
        return

    visited[x] = 0
    for k in arr[x]:
        if visited[k] == -1: # 방문 하지 않은 곳이면, 재귀 호출. cnt 증가
            DFS(k, st_i, cnt + 1)
            if not ans:
                visited[k] = -1
        elif visited[k] == 0 and k == st_i and cnt >= 3:
            ans = True
            return

n = int(input())
arr = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
ans = False

for _ in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,n+1):
    if visited[i] == -1:
        DFS(i, i, 1)
        if ans == True:
            break

from collections import deque
def BFS(j):
    visited[j] = 0
    dq = deque()
    dq.append([j, 0])

    while dq:
        x_num, cnt = dq.popleft()
        for k in arr[x_num]:
            if visited[k] == 0:
                # j : 처음 값을 인덱스로 사용하여 거리를 저장한다.
                visited[j] = cnt + 1
                break
            elif visited[k] != 0 or visited[k] == -1:
                dq.append([k, cnt + 1])
print(visited)
for j in range(1, n+1):
    if visited[j] == -1:
        BFS(j)
    print(visited[j], end=' ')

