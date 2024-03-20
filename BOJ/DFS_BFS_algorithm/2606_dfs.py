c = int(input())
n = int(input())

graph = [[0]*(c+1) for _ in range(c+1)]
for i in range(n):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False] * (c+1)
cnt = 0
def dfs(f):
    visited[f] = True
    global cnt

    for j in range(c+1):
        if graph[f][j] == 1 and visited[j] == False:
            cnt += 1
            dfs(j)

dfs(1)
print(cnt)