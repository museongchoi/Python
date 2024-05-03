# 이분 그래프
# 문제.
# k : 테스트 케이스 개수, v : 정점의 개수, e : 간선의 개수
# 1. 긱 정점은 1부터 ~ v까지 번호가 붙어 있다.
# 2. 각 테스트 케이스 첫째줄에는 v e,
# 3. 둘째줄에는 간선에 대한 정보 x, y 주어진다.

# 이분 그래프 탐색 방법
# 1. 최초 탐색 시작할 정점의 색상을 빨간색으로 칠한다.(숫자 1로 표현)
# 2. 최초 정점의 인접 정점의 색상을 파란색으로 칠한다.(숫자 -1로 표현)
# 3. 해당 인접 정점들을 차례로 탐색을 시작하며 자신과 인접한 정점을 빨간색으로 칠한다.(숫자 1로 표현)
# 4. 이와 같은 방식을 탐색을 지속하며 반복하여 2개의 색상으로 모두 칠한다.
# 5. 색상을 칠하다가 이웃 정점이 같은 색으로 칠해져 있다면 이분 그래프가 될 수 없다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000) # v(정점)가 최대 20000개

def DFS(a, group):
    global ans
    if ans: # ans == True 이면, DFS 탐색 종료. 재귀 함수의 리턴 값이 이분 그래프가 아니면 리턴을 하기 때문에 ans 값을 확인 한다.
        return
    visited[a] = group
    for b in graph[a]:
        if not visited[b]:  # visited[b] == False 이면, 방문하지 않은 곳.
            DFS(b, -group)  # b 와 처음 1(빨강)이 저장되어 있기 때문에 -1 을 곱하여 현재 색의 반대색을 칠해준다.
        elif visited[b] == visited[a]:  # 방문한 곳이고, 같은 그룹이라면 이분 그래프가 아니므로 True를 리턴, 재귀 리턴 값이다.
            ans = True
            return

# 테스트 케이스 횟수 k
k = int(input())

for _ in range(k):
    v, e = map(int, input().split())    # v : 노드 개수, e : 간선의 개수
    graph = [[] for _ in range(v+1)]    # graph : idx 를 노드로 활용, 각 노드의 간선 정보를 저장
    visited = [False] * (v+1)           # 방문 체크 및 빨간색, 파란색 체크
    ans = False # 이분 그래프 여부, False : 이분 그래프이다, True : 이분 그래프가 아닌 것을 찾아냄.

    for _ in range(e):
        x, y = map(int, input().split())
        # 양방향성
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v+1):
        if visited[i] == False: # 첫번째 노드 부터 탐색 시작, 방문하지 않은 노드를 탐색.
            DFS(i, 1)
            if ans: # in ans == True:, 이면 반복문 종료
                break

    if ans:
        print('NO')
    else:
        print('YES')
