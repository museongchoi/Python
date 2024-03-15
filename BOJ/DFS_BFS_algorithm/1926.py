# 그림
from collections import deque
def bfs(x, y):
    a[x][y] = 0
    tmp = 1
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        if 0 <= x-1 < n and a[x-1][y] == 1:
            q.append([x-1, y])
            a[x-1][y] = 0
            tmp += 1
        if 0 <= x+1 < n and a[x+1][y] == 1:
            q.append([x+1, y])
            a[x+1][y] = 0
            tmp += 1
        if 0 <= y-1 < m and a[x][y-1] == 1:
            q.append([x, y-1])
            a[x][y-1] = 0
            tmp+=1
        if 0 <= y+1 < m and a[x][y+1] == 1 :
            q.append([x, y+1])
            a[x][y+1] = 0
            tmp+=1

    return tmp

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0 # 그림 개수
ans = 0 # 제일 큰 그림 넓이
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            cnt += 1
            ans = max(bfs(i, j), ans)

print(cnt)
print(ans)
