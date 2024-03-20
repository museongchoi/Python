from collections import deque

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
amap = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    visited[x][y] = True
    dq = deque()
    dq.append([x, y])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if x == n-1 and y == m-1:
                print(amap[n-1][m-1])
                return

            if 0 <= nx < n and 0 <= ny < m:
                if amap[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    amap[nx][ny] = amap[x][y] + 1
                    dq.append([nx, ny])


bfs(0,0)
