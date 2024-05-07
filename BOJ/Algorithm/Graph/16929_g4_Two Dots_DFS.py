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
            if visited[nx][ny]:
                if cnt >= 4 and nx == st_x and ny == st_y:
                    ans = True
                    return
            elif maps[nx][ny] == maps[st_x][st_y]:
                DFS(nx, ny, cnt+1, st_x, st_y)
    visited[x][y] = False

n, m = map(int, input().split())
maps = [list(map(str, input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = False  # False : 사이클이 아님, True : 사이클을 발견함.

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            st_i = i
            st_j = j
            DFS(i, j, 1, st_i, st_j)
            if ans:
                print('Yes')
                sys.exit(0)

print('No')

# 방법2
# Two Dots
# import sys
# input = sys.stdin.readline
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# def DFS(x, y, cnt, st_x, st_y):
#     global ans
#     if ans:
#         return
#
#     visited[x][y] = True
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if cnt >= 4 and nx == st_x and ny == st_y:
#                 ans = True
#                 return
#             if maps[nx][ny] == maps[st_x][st_y] and visited[nx][ny] == False:
#                 DFS(nx, ny, cnt+1, st_x, st_y)
#     visited[x][y] = False
#
# n, m = map(int, input().split())
# maps = [list(map(str, input().strip())) for _ in range(n)]
# visited = [[False]*m for _ in range(n)]
# ans = False  # False : 사이클이 아님, True : 사이클을 발견함.
#
# for i in range(n):
#     for j in range(m):
#         st_i = i
#         st_j = j
#         DFS(i, j, 1, st_i, st_j)
#         if ans:
#             print('Yes')
#             sys.exit(0)
#
# else:
#     print('No')

# 방법 1
# Two Dots
# import sys
#
# input = sys.stdin.readline
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# ans = False  # False : 사이클이 아님, True : 사이클을 발견함.
#
#
# def DFS(x, y, cnt, st_x, st_y):
#     global ans
#     if cnt >= 4 and x == st_x and y == st_y:
#         ans = True
#         return
#
#     visited[x][y] = True
#
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == maps[st_x][st_y]:
#             if visited[nx][ny] == False:
#                 DFS(nx, ny, cnt + 1, st_x, st_y)
#
#             elif cnt >= 4 and nx == st_x and ny == st_y:
#                 ans = True
#                 return
#     visited[x][y] = False
#
#
# n, m = map(int, input().split())
# maps = [list(map(str, input().strip())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# cnt = 1
#
# for i in range(n):
#     for j in range(m):
#         if visited[i][j] == False:
#             st_i = i
#             st_j = j
#             DFS(i, j, cnt, st_i, st_j)
#         if ans:
#             print('Yes')
#             exit()
#
# else:
#     print('No')