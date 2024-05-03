# 단지 번호 붙이기 - DFS
# 1 : 집이 있는 곳, 0 : 집이 없는 곳
# 좌 우 위 아래만 연결되어 있는 것
# n*n 크기의 정사각형
# 총 단지수, 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력

import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().strip())) for _ in range(n)] # 아래 코드와 동일
# maps = []
# for _ in range(n):
#     maps.append(list(map(int, input().strip())))
#
# print(maps)
visited = [[False]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y):
    global count
    count += 1
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                DFS(nx, ny)

cnt = 0 # 단지 수
alist = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == False:
            count = 0
            cnt += 1
            DFS(i, j)
            alist.append(count)


alist.sort()
print(cnt)
for j in alist:
    print(j)


