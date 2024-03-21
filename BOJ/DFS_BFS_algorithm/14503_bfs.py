# 1 현재 위치 출발, 청소 후 q에 넣고 시작
# 2 현재 위치 청소 여부 확인, 청소 후 전진 방향 선택
# 3 각 방향 마다 벽 and 청소 여부 확인
# 4 다 되어 있으면
# 4-1 현재 방향 유지 한채로 한칸 후진 후 2번으로 돌아감
# 4-2 바라 보는 방향 뒤 쪽이 벽이면 작동 멈춤
# 5 청소 되지 않은 빈칸이 있으면
# 5-1 90도 회전 반시계 방향
# 5-2 바라보는 방향 기준 앞이 빈칸인 경우 전진
# 5-3 2번으로 돌아감

from collections import deque
N, M = map(int, input().split())    # graph 크기 세로, 가로
r,c,d = map(int, input().split())   # 현재 좌표, 방향
graph = [list(map(int, input().split())) for _ in range(N)]

# 0 : 빈칸(청소x), 1 : 벽, 2 : 청소 완
# d = 0 : 북쪽/x-1, 1 : 동쪽/y+1, 2 : 남쪽/x+1, 3 : 서쪽 y-1
# 북0 동1 남2 서3
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,d):
    cnt = 0
    dq = deque()
    # 시작 위치 삽입
    dq.append([x, y, d])
    graph[x][y] = 2
    cnt += 1

    while dq:
        x, y, d = dq.popleft()
        tmp_d = d   # 현재 d 값 보존
        turn = 0    # 연속 회전 횟수

        for i in range(4):
            nd = (tmp_d + 3) % 4    # d = 0 북 일때 (0+3) % 4 = 3 서 / nd 는 idx 로 활용 가능, 검사 해야할 방향
            nx = x + dx[nd]
            ny = y + dy[nd]
            tmp_d = nd

            if 0 <= nx < N and 0 <= ny < M: # 범위 체크
                if graph[nx][ny] == 0:  # 빈칸(청소 x) 일때
                    graph[nx][ny] = 2   # 청소 완, 방문 처리
                    cnt += 1    # 청소 횟수 증가
                    dq.append([nx, ny, tmp_d])  # 전진
                    break   # 1칸 전진한 칸에서 다시 검사하기 위해
                else:   # 벽이거나 청소 완 칸이면 회전
                    turn += 1

        if turn == 4:
            idx = (d + 2) % 4  # d 가 0 북 일때 (0+2) % 4 = 2 남, 반대 편이 나와야 한다. 북 <=> 남 / 동 <=> 서
            bx = x + dx[idx]
            by = y + dy[idx]

            # bx, by 의 범의 조건은 앞서 전진 범위 조건이 맞으면 turn을 하므로 없어도 됨.
            if graph[bx][by] == 1: # 반대편이 벽이면 종료 다 청소인 상태이면 dq 에 추가
                return cnt

            dq.append([bx, by, d]) # 후진, 바라보는 방향 그대로 후진이므로 방향 고정


# r,c,d = 1 1 0
result = bfs(r, c, d)
print(result)
