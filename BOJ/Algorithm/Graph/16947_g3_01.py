def DFS(x, start, cnt):
    global ans
    if ans:
        return

    for y in graph[x]:
        if visited[y] == False:
            visited[y] = True
            DFS(y, start, cnt + 1)
            if not ans:
                visited[y] = False
        elif y == start and cnt >= 3:
            ans = True
            return


n = int(input())
graph = [[] for _ in range(n+1)] # 노드 연결 정보
cycle_st = [False] * (n+1) # 순환선 체크
distance = [-1] * (n+1) # 지선에서 순환까지 거리 체크

for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
for i in range(1, n+1):
    visited = [False] * (n+1)
    ans = False
    DFS(i, i, 1)
    print(visited)
    if ans:
        break
