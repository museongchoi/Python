# 섬의 개수
# 지도, 섬 : 1, 바다 : 0
# 섬은 가로, 세로, 대각선으로 걸어서 갈 수 있는 경로가 있어야 한다.
# 총 8개의 구간을 검사 : 좌, 우, 위, 아래, 대각선 4방향
# 첫째 줄은 w : 너비, h : 높이
# 둘째 줄부터 h개 줄에는 지도가 주어진다.
# 입력의 마지막은 0 두개
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    def BFS(x, y):
        visited[x][y] = True
        dq = deque()
        dq.append([x, y])

        while dq:
            a, b = dq.popleft()
            for k in range(8):
                nx = a + dx[k]
                ny = b + dy[k]
                if 0 <= nx < h and 0 <= ny < w:
                    if maps[nx][ny] == 1 and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        dq.append([nx, ny])

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                BFS(i, j)

    print(cnt)
