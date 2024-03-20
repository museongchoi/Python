from collections import deque

n,m,v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)] # 연결 노드 체크 그래프 생성

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1 # 간선 양방향

# 방문 리스트
visited1 = [False] * (n+1)
visited2 = visited1.copy()

#dfs
def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for j in range(1, n+1):
        if graph[v][j] == 1 and visited1[j] == False:
            dfs(j)

#bfs
def bfs(v):
    visited2[v] = True
    dq = deque()
    dq.append(v)

    while dq:
        tmp = dq.popleft()
        print(int(tmp), end=' ')
        for i in range(1, n+1):
            if graph[tmp][i] == 1 and visited2[i] == False:
                visited2[i] = True
                dq.append(i)

dfs(v)
print()
bfs(v)
