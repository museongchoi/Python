# 연결 요소의 개수
# 방향이 없다. n : 정점의 개수, m : 간선의 개수
# 출력 : 연결 요소의 개수를 구하라.
# 방문 체크를 하고 초기화 할 필요 없다. 방문한 곳을 방문하면 안됨.

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False] * (n+1)

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def BFS(a):
    visited[a] = True
    dq = deque()
    dq.append(a)

    while dq:
        a = dq.popleft()
        for b in range(1, n+1):
            if graph[a][b] == 1 and visited[b] == False:
                visited[b] = True
                dq.append(b)


cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        BFS(i)
        cnt += 1

print(cnt)