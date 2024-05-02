# 이분 그래프
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
from collections import deque
input = sys.stdin.readline

def BFS(start, group):
    dq = deque()
    dq.append(start)
    visited[start] = group

    while dq:
        a = dq.popleft()
        for b in range(1, v + 1):
            if graph[a][b] == 1:
                if visited[b] == False:
                    visited[b] = -1 * visited[a]
                    dq.append(b)
                elif visited[b] == visited[a]:
                    return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    # 노드 인접 정보
    graph = [[0]*(v+1) for _ in range(v+1)]
    # 방문 체크 0, 빨 : 1, 파 : -1
    visited = [False] * (v+1)

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1

    for i in range(1, v+1):
        if visited[i] == False:
            result = BFS(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
