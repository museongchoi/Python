# 네트워크
from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(idx):
        dq = deque()
        visited[idx] = True
        dq.append(idx)

        while dq:
            idx = dq.popleft()

            for i in range(n):
                if computers[idx][i] == 1 and visited[i] == False:
                    visited[i] = True
                    dq.append(i)

    for i in range(n):
        # 방문하지 않은 컴퓨터를 찾는다. 해당 컴퓨터에 네트워크로 연결되어있는 모든 컴퓨터들을 방문 체크
        if not visited[i]:
            answer += 1
            bfs(i)

    return answer

# 문제 풀이
# 0~n까지의 값들이 곧 컴퓨터를 말함.
# bfs 함수 예 : 0번 컴퓨터에 네트워크로 연결된 컴퓨터들을 모두 방문체크 하고 빠져나온다.
# 네트워크의 종류 개수라고 생각하기.
