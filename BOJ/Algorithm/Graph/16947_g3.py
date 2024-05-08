# 서울 지하철 2호선
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def DFS(idx, st_idx, cnt):
    global ans
    if st_idx == idx and cnt >= 2:
        ans = True
        return

    visited[idx] = True
    for k in arr[idx]:
        if visited[k] == False: # 방문 하지 않은 곳이면, 재귀 호출. cnt 증가
            DFS(k, st_idx, cnt + 1)
        elif k == st_idx and cnt >= 2:
            DFS(k, st_idx, cnt)

def BFS():
    global ck
    dq = deque()
    for i in range(1, n+1):
        if cycle_st[i]:
            ck[i] = 0
            dq.append(i)

    while dq:
        x_idx = dq.popleft()
        for k in arr[x_idx]:
            # -1 인 값을 큐에 넣는다.
            if ck[k] == -1:
                dq.append(k)
                ck[k] = ck[x_idx] + 1

    for j in ck[1:]:
        print(j, end=' ')

n = int(input()) # 역 개수 입력받기
arr = [[] for _ in range(n+1)]  # 역과 역을 연결하는 구간의 정보
cycle_st = [False]*(n+1) # 순환역 표시하는 전체 역
ck = [-1] * (n+1) # 거리 저장

for _ in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,n+1):
    visited = [False] * (n + 1)
    ans = False
    DFS(i, i, 0)
    if ans:
        cycle_st[i] = True

BFS()
