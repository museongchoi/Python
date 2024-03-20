from collections import deque
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
visited = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0 # 단지수
ans = [] # 단지내 집 크기를 정렬

def bfs(x, y):
    count = 1
    visited[x][y] = True
    dq = deque()
    dq.append([x, y])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    dq.append([nx, ny])
                    count += 1

    ans.append(count)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            bfs(i, j)

ans.sort()
print(cnt)
for h in range(len(ans)):
    print(ans[h])