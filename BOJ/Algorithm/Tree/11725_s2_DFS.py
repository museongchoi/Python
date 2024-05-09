# 트리의 부모 찾기
# 루트 노드가 1이라고 가정 했을때, 출력은 2번 노드부터 n노드까지 부모노드를 출력.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = [0]*(n+1)


for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def DFS(root):
    visited[root] = True
    # ans 자식에 root를 저장
    for k in tree[root]:
        if visited[k] == False:
            ans[k] = root
            DFS(k)

DFS(1)

for i in range(2, n+1):
    print(ans[i])