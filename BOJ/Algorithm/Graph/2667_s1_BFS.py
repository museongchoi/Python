# 단지 번호 붙이기 - BFS
# 1 : 집이 있는 곳, 0 : 집이 없는 곳
# 좌 우 위 아래만 연결되어 있는 것
# n*n 크기의 정사각형
# 총 단지수, 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력

import sys
from collections import deque
n = int(input())

maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    global count
    count += 1
    visited[x][y] = True
    dq = deque()
    dq.append([x,y])

    while dq:
        a, b = dq.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    count += 1
                    dq.append([nx, ny])


cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == False:
            count = 0
            cnt += 1
            BFS(i, j)
            ans.append(count)

ans.sort()
print(cnt)
for j in ans:
    print(j)