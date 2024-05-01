# ABCDE
# a-b-c-d-e 의 관계가 입력에 존재하면 1, 아니면 0
# 탐색 노드에서 깊이 우선인 DFS 를 활용, 깊이가 5이상이면 break 성공하는것.
# 깊이가 5인 상황이 한번이라도 나오면 성공.
# n : 인원수, m : 관계수
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

maps = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    maps[x].append(y)
    maps[y].append(x)

ans = False # 성공 여부
visited = [False] * n  # 방문체크
depth = 1  # 5이상이면 성공
def dfs(x, depth):
    global ans
    visited[x] = True
    if depth >= 5:
        ans = True
        return
    for k in maps[x]:
        if visited[k] == False:
            dfs(k, depth+1)
    visited[x] = False

# 방문 초기화를 dfs 실행이 될때마다 초기화 하지 않는 이유. 깊이 탐색을 한 뒤에 돌아오면서 초기화 하는 이유.
# 탐색이 끝나면 방문 초기화를 해야 해당 노드가 연결되어 있는 노드들을 방문할 수 있다.
# 그렇지 않으면 다시 돌아 왔을때 앞서 방문 탐색한 부분에서 방문체크가 되어있으면 해당 노드를 탐색하지 않기 때문이다.
# 굿노트/노션 참고

# 특정 노드 기준 친구 관게를 확인 하기 위해 n 반복
for i in range(n):
    dfs(i, depth)
    if ans:
        break

if ans:
    print(1)
else:
    print(0)