from collections import deque
c = int(input())
n = int(input())

# 컴퓨터의 개수가 c 개 1번 컴퓨터부터 시작, idx 는 0번 부터 시작 이므로 +1 한다
graph = [[0]*(c+1) for _ in range(c+1)]
for i in range(n):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

# 컴퓨터의 개수만큼 방문 체크 생성
visited = [False] * (c+1)
cnt = 0

def bfs(v):
    visited[v] = True
    global cnt
    dq = deque()
    dq.append(v)

    while dq:
        v = dq.popleft()
        for j in range(c+1):
            if graph[v][j] == 1 and visited[j] == False:
                visited[j] = True
                dq.append(j)
                cnt += 1

    return cnt


print(bfs(1))