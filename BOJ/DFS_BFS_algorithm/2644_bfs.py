from collections import deque

n = int(input())
n1, n2 = map(int, input().split())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False]*(n+1)

def bfs(n1):
    visited[n1] = True
    dq = deque()
    dq.append([n1, 0])

    while dq:
        tmp, dist = dq.popleft()
        if tmp == n2:
            return dist
        for i in range(1, n+1):
            if graph[tmp][i] == 1 and visited[i] == False:
                visited[tmp] = True
                dq.append([i, dist + 1])


result = bfs(n1)
if result != None:
    print(result)
else:
    print(-1)