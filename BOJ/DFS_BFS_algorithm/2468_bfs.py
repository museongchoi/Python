from collections import deque
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

def bfs(x, y, visited, k):
    visited[x][y] = True
    dq = deque()
    dq.append([x,y])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] > k and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    dq.append([nx, ny])

tmp = 0
for k in range(maxNum):
    cnt = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == False:
                cnt += 1
                bfs(i, j, visited, k)

    if tmp < cnt:
        tmp = cnt

print(tmp)