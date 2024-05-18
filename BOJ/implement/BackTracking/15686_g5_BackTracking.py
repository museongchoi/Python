# 치킨 배달
# n * n 도시, (r,c) 형태, r과c는 1부터 시작
# 최대 m개의 치킨 집 제외 나머지 폐업시킴.
# 빈칸 : 0, 집 : 1, 치킨집 : 2

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

ck_map = []
ck_list = []
for i in range(n):
    ck_map.append(list(map(int, input().split())))
    for j in range(n):
        if ck_map[i][j] == 2:
            ck_list.append([i,j])
visited = [False]*len(ck_list)
ans = 1e9

def BackTracking(cnt, start):
    global ans
    if cnt == m:
        total = 0
        for i in range(n):
            for j in range(n):
                if ck_map[i][j] == 1: # 집을 찾았을 때
                    min_dist = 1e9
                    for k in range(len(ck_list)):
                        if visited[k]:  # 현재 선택된 치킨 집을 찾는다.
                            x, y = ck_list[k]
                            dist = abs((i+1)-(x+1)) + abs((j+1)-(y+1))
                            min_dist = min(min_dist, dist) # 현재 집에서 최소 치킨 거리를 구한다.
                    total += min_dist # total에 현재 집의 최소 치킨 거리를 더해준다.
        # 각 집의 최소 치킨 거리를 구하여 현재 선택된 치킨 집일 경우 total을 구했으므로 앞서 다른 치킨집의 경우 total 값과 현재 치킨집을 고른 경우 total 값을 비교하여 갱신한다.
        ans = min(ans, total)
        return

    for idx in range(start, len(ck_list)):
        if not visited[idx]:
            visited[idx] = True
            BackTracking(cnt + 1, idx + 1)
            visited[idx] = False

BackTracking(0, 0)
print(ans)