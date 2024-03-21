# M, N, H = map(int, input().split())
#
# graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# visited = [[[False]*M for _ in range(N)] for _ in range(H)]
#
# dx = [-1,1,0,0,0,0]
# dy = [0,0,-1,1,0,0]
# dk = [0,0,0,0,-1,1]
# 
# def bfs(x,y,k):
#
#
# for k in range(H):
#     for i in range(N):
#         for j in range(M):
#             if graph[k][i][j] == 1 and visited[k][i][j] == False:
#                 bfs(k,i,j)
#
# print(graph)
# print(visited)