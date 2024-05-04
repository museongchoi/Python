# Two Dots
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y, cnt, st_x, st_y):
    global ans
    if ans:
        return

    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if cnt >= 4 and nx == st_x and ny == st_y:
                ans = True
                return
            if maps[nx][ny] == maps[st_x][st_y] and visited[nx][ny] == False:
                DFS(nx, ny, cnt+1, st_x, st_y)
    visited[x][y] = False

n, m = map(int, input().split())
maps = [list(map(str, input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = False  # False : 사이클이 아님, True : 사이클을 발견함.

for i in range(n):
    for j in range(m):
        st_i = i
        st_j = j
        DFS(i, j, 1, st_i, st_j)
        if ans:
            print('YES')
            sys.exit(0)

else:
    print('NO')