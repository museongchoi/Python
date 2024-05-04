# 나이트 이동
# t : 테스트 케이스
# 1. l : 한 변의 길이, 체스판 크기 : l * l
# 2. 나이트 현재 위치
# 3. 나이트가 이동할 위치
import sys
input = sys.stdin.readline
from collections import deque

# 각 방향 총 검사 회수는 한 위치당 8개
dx = [-1, -2, -2, -1, 1, 2, 2, 1]   # 이동 가능 x 좌표
dy = [-2, -1, 1, 2, 2, 1, -1, -2]   # 이동 가능 y 좌표

def BFS(s_x, s_y):
    visited[s_x][s_y] = True
    dq = deque()
    dq.append([s_x, s_y])

    while dq:
        i, j = dq.popleft()

        if i == a and j == b:
            return maps[i][j]

        for k in range(8):  # x, y 이동 방향
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == False:    # 범위 체크, 방문 체크
                visited[nx][ny] = True  # 방문 체크
                maps[nx][ny] = maps[i][j] + 1   # 최단 거리를 좌표 값을 이용, 다음 최단 거리를 계산하여 저장.
                dq.append([nx, ny])


t = int(input())
for _ in range(t):
    l = int(input())
    maps = [[0]*l for _ in range(l)]
    # maps1 = [[0 for _ in range(l)] for _ in range(l)] # maps와 동일 코드
    visited = [[False]*l for _ in range(l)]

    x, y = map(int, input().split()) # 시작 지점
    a, b = map(int, input().split()) # 도착 지점

    ans = BFS(x, y)
    print(ans)