# n*n 공간
# m 마리 물고기, 아기 상어 1마리 (처음 크기 2)
# 아기 상어는 상 하 좌 우 한칸씩 이동 가능, 이동 할때 1초가 걸리는데 1동하면서 먹을 수 있는 물고기이면 먹는다.(먹을때 시간이 걸리진 않음)
# 아기 상어는 자신보다 큰 물고기 칸은 지나갈 수 없다. 나머지는 지나갈 수 있음.
# 즉, 자신과 크기가 같으면 지나갈 수는 있고, 크기가 작다면 먹을 수 있음, 먹으면 그 칸은 0이 된다.

# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
# 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
# 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하라.

# 0: 빈 칸, 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기, 9: 아기 상어의 위치
# 이동 결정 조건
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
w_map = []
shark_x = 0
shark_y = 0
for i in range(n):
    w_map.append(list(map(int, input().split())))
    if 9 in w_map[i]:
        shark_x, shark_y = i, w_map[i].index(9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 아기 상어 조건에 맞는 물고기 최단 거리 먹이 구하기
def BFS(x, y):
    w_visited_move = [[0] * n for _ in range(n)]  # 0 일때는 방문하지 않은 곳
    food_list = []    # return move, x, y
    dq = deque()
    dq.append([x, y])
    w_visited_move[x][y] = 1 # 방문체크를 할겸 거리 갱신

    while dq:
        i, j = dq.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            # nx, ny 범위 확인, 방문하지 않았을때
            if 0 <= nx <n and 0 <= ny <n and w_visited_move[nx][ny] == 0:
                if w_map[x][y] > w_map[nx][ny] and w_map[nx][ny] != 0: # 상어가 물고기보다 클 때, 물고기를 먹을 수 있다.
                    w_visited_move[nx][ny] = w_visited_move[i][j] + 1
                    # 현재 상어가 먹을 수 있는 물고기이므로 최단 거리를 구해야한다. cand[2]에 가장 작은 최단 거리 추가
                    food_list.append((w_visited_move[nx][ny] - 1, nx, ny))
                elif w_map[x][y] == w_map[nx][ny]:  # 상어와 물고기가 크기가 같을때, 움직이기만 한다.
                    w_visited_move[nx][ny] = w_visited_move[i][j] + 1
                    dq.append([nx, ny])
                elif w_map[nx][ny] == 0:    # 움직이는 곳이 비어 있을때.
                    w_visited_move[nx][ny] = w_visited_move[i][j] + 1
                    dq.append([nx, ny])

    return sorted(food_list, key=lambda x : (x[0], x[1], x[2]))

# 상어의 크기를 현재 상어 위치로 갱신
# BFS 실행 방문
# 현재 위치 방문 체크 후 dq에 x,y,move 값 넣고

# x, y : 상어 좌표, cnt : 걸린 시간, s_size : 상어 크기, s_cnt : 잡아먹은 물고기 수(상어 레벨업 확인)
s_size = [2, 0] # s_size[0] : 상어 사이즈, s_size[1] : 상어가 물고기를 먹은 횟수
cnt = 0 # 엄마 상어를 부르는데 걸린 시간
while True:
    w_map[shark_x][shark_y] = s_size[0] # 상어 현재 위치 크기로 갱신
    ans = deque(BFS(shark_x, shark_y))    # cand = shark_x, shark_y, s_move

    # 반환 값이 없으면 먹이가 없다는 것, cand[2] move 가 0이면 움직이지 못한 것 먹이가 없는 것이므로 break로 변경 가능할지도?
    if not ans:
        break

    s_size[1] += 1  # BFS 탐색을 했다면 먹이를 먹은 것이므로 1 증가.
    move, xx, yy = ans.popleft()
    cnt += move # 상어가 움직인 거리(시간)를 더해준다.
    # print('cnt',cnt)
    # print('move', move)
    w_map[shark_x][shark_y] = 0  # 현재 상어가 물고기를 먹은 위치를 0으로. whlie문으로 반복 시 상어의 현재 위치가 되어 상어 크기로 다시 갱신 된다.
    shark_x, shark_y = xx, yy

    # 상어가 먹이를 먹은 횟수와 현재 상어 크기가 같으면, 상어 크기 갱신 후 먹은 횟수 리셋
    if s_size[0] == s_size[1]:
        s_size[0] += 1
        s_size[1] = 0

print(cnt)

