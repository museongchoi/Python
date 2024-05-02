# 연결 요소의 개수
# 방향이 없, n : 정점의 개수, m : 간선의 개수
# 출력 : 연결 요소의 개수를 구하라.
# 방문 체크를 하고 초기화 할 필요 없다. 방문한 곳을 방문하면 안됨.
# 방법 2 : append 사용
import sys
# 재귀 깊이 초과
# Python의 기본 재귀 깊이 제한은 약 1000입니다. 이 문제에서 연결 요소를 찾기 위해 DFS (깊이 우선 탐색)를 사용하면,
# 큰 그래프에서 깊은 재귀 호출이 필요할 수 있습니다. 이 경우 기본 재귀 한도를 초과하여 RecursionError가 발생할 수 있습니다.
# 해결 방법
# Python에서 재귀 호출의 깊이 제한을 늘리기 위해 sys.setrecursionlimit() 함수를 사용할 수 있습니다.
# 이 함수를 사용하여 재귀 깊이를 적절히 늘리면 문제를 해결할 수 있습니다.
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)

graph = list([] for _ in range(n+1))
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(a):
    visited[a] = True
    for j in graph[a]:
        if visited[j] == False:
            dfs(j)

cnt = 0
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)

# 방법 1 : 0으로 초기화한 리스트를 사용 1로 체크
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
#
# n, m = map(int, input().split())
#
# maps = [[0]*(n+1) for _ in range(n+1)]
# visited = [False] * (n+1)
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     maps[x][y] = maps[y][x] = 1
#
# #print(maps)
# def dfs(x):
#     visited[x] = True
#     for j in range(1, n+1):
#         if maps[x][j] == 1 and visited[j] == False:
#             dfs(j)
#
#
# # 모든 노드가 연결되어 있지 않기 때문에 순회하면서 해당 노드를 dfs 함수 활용하여 검사한다.
# cnt = 0
# for i in range(1, n+1):
#     if visited[i] == False:
#         dfs(i)
#         cnt += 1
#
# print(cnt)