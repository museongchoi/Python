# 스타트와 링크
# 총 4명이 2명씩 한팀이 될때 스타트팀과 링크팀의 최소 능력치 차이를 구하라.
# s[i,j] 와 s[j,i] 팀이 된다고 했을 때 좌표에 있는 능력치를 서로 합하고, s[a,b] + s[b,a] 능력치의 합을 구하여
# 두팀의 최소 능력치 차이를 구한다.
import sys
input = sys.stdin.readline
n = int(input()) # n 명의 사람들이 팀을 나누기 위해서는 n//2로 팀을 정한다. n*n으로 능력치가 주어진다.
player = [list(map(int, input().split())) for _ in range(n)] # 능력치 그래프
visited = [False for _ in range(n)] # 1차원 방문 체크
ans = sys.maxsize

def backtracking(cnt, idx):
    global ans
    # n//2 개의 팀으로 True와 False로 나누어지면 실행되는 조건.
    # True(스타트팀) False(링크팀)의 각 능력치 합을 구하고, 두 팀의 차를 구한다.
    if n//2 == cnt:
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += player[i][j]
                elif not visited[i] and not visited[j]:
                    b += player[i][j]
        # 최소 차를 저장 한다.
        ans = min(ans, abs(a-b))
        return
    # 1,2,3,4 명이 있을때 1,2 / 3,4 || 1,3 / 2,4 등등 1번 사람과 팀이 되는 경우, 2번 사람과 팀이 되는 경우
    # 모든 경우에 수를 구한다.
    for k in range(idx, n):
        if not visited[k]:
            # 방문 체크를 한 뒤에 재귀함수로 들어가 n//2 팀으로 분리 되었는지 확인한다.
            visited[k] = True
            backtracking(cnt+1, k+1)
            # 최소 값을 구한 뒤에는 방문 체크를 풀어준다.
            # ex) 1번 사람과 팀이 되었을 경우를 확인 한뒤에 기준이 2번 사람과 팀이 되었을 경우를 확인 해야하기 때문이다.
            visited[k] = False

backtracking(0,0) # 재귀 적으로 모든 경우에 수를 확인해야 한다.
print(ans)
