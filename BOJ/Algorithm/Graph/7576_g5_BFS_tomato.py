# 토마토, BFS 너비 우선 탐색이 탁월함.
# 첫째 줄은 m : 가로 칸수, n : 세로 칸 수
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어 있지 않음
# 토마토가 모두 익을 때까지의 최소 날짜를 출력
# 저장될때부터 모두 익어 있는 상태이면 0을 출력, 모두 익지 못하는 상황이면 -1 출력

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def BFS():
    while dq:
        x, y = dq.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    dq.append([nx, ny])

dq = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append([i, j])

BFS()
cnt = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    cnt = max(cnt, max(i))
else:   # 루프가 정상적으로 완료되었을때 실행.
    print(cnt - 1)

# 탈출 조건을 내/외부로 관리
# cnt = 0
# terminated = False  # 루프 탈출을 관리하는 플래그.
# for i in tomato:
#     if terminated:  # 외부 루프 탈출 조건.
#         break
#     for j in i:
#         if j == 0:
#             print(-1)
#             terminated = True   # 내부 루프에서 탈출 상태 설정.
#             break
#     cnt = max(cnt, max(i))
# else:   # 루프가 정상적으로 완료되었을때 실행.
#     print(cnt - 1)


