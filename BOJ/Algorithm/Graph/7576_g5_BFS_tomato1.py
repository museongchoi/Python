from collections import deque

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS():
    dq = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                dq.append([i,j])

    while dq:
        x, y = dq.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1
                dq.append([nx,ny])

BFS()
day = 1
for li in maps:
    if 0 in li:
        print(-1)
        break
    for lj in li:
        day = max(day, lj)
else:
    print(day-1)

