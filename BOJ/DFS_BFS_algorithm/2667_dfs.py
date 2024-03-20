N = int(input())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
ans = []
count = 0
for _ in range(N):
    graph.append(list(map(int, input())))
visited = [[False]*N for _ in range(N)]

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            count = 0
            cnt += 1
            dfs(i, j)
            ans.append(count)

ans.sort()
print(cnt)
for h in range(len(ans)):
    print(ans[h])