import sys
sys.setrecursionlimit(100000)

N = int(input())

maxNum = 0
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if maxNum < graph[i][j]:
            maxNum = graph[i][j]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y, k):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] > k and visited[nx][ny] == False:
                dfs(nx, ny, k)

result = 0
for k in range(maxNum):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == False:
                cnt += 1
                dfs(i, j, k)

    result = max(result, cnt)

print(result)