n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

visited = [False]*(n+1)
# == visited2 = [False for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

flag = False # b 를 발견했는지 여부
def dfs(xa, cnt):
    global flag
    visited[xa] = True
    if xa == b:
        flag = True
        print(cnt)
    for val in graph[xa]:
        if visited[val] == False:
            dfs(val, cnt+1)

dfs(a, 0)

if flag == False:
    print(-1)
