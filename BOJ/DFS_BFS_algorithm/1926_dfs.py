# # 그림
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
# from collections import deque
#
# def dfs(graph, x, y, visited):
#
#
#
#
#
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
#
# cnt = 0 # 그림 개수
# ans = 0 # 그림 크기
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1 and visited[i][j] == 0:
#             visited[i][j] = 1
#             ans = max(dfs(graph, i, j, visited), ans)
#             cnt += 1
#
# print(n, m)
# print(a)