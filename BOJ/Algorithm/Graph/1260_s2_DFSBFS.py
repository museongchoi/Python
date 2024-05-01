# DFS 와 BFS
# N : 노드 개수, M : 간선의 개수, V : 시작점

from collections import deque
n, m, v = map(int, input().split())

maps = [[] for _ in range(n)]
visited1 = [False] * n
visited2 = visited1.copy()

for i in range(m):
    x, y = map(int, input().split())
    maps[x].append(y)
    maps[y].append(x)

def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in maps[v]:
        if visited1[i] == False:
            dfs(i)


def bfs(v):
    visited2
    dq = deque()
    dq.append(v)

    while dq:
        tmp = dq.popleft()
        print(tmp, end=' ')

dfs(v)
print()
bfs(v)