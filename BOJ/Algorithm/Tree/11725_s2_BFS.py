# 트리의 부모 찾기
# 루트 노드가 1이라고 가정 했을때, 출력은 2번 노드부터 n노드까지 부모노드를 출력.

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = [0]*(n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def BFS(root):
    visited[root] = True
    dq = deque()
    dq.append(root)

    while dq:
        x = dq.popleft()
        for k in tree[x]:
            if visited[k] == False:
                visited[k] = True
                dq.append(k)
                ans[k] = x

BFS(1)
for i in range(2, n+1):
    print(ans[i])