# 촌수 계산
n = int(input())
a, b = map(int, input().split())
m = int(input())

# idx 1 부터 시작하기 때문 n+1만큼의 공간을 만들어준다. 가족 관계를 1로 체크 해놓을 그래프 변수
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False]*(n+1)

tmp = False
def dfs(a, cnt):
    global tmp
    visited[a] = True

    if a == b:
        tmp = True
        print(cnt)

    for i in range(1, n+1):
        if graph[a][i] == 1 and visited[i] == False:
            dfs(i, cnt + 1)


dfs(a, 0)
if tmp == False:
    print(-1)