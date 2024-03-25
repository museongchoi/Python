# 아이템 줍기
# 2배를 하는 이유는 1칸짜리 ㄷ자 모양을 돌아갈 때 회전구간 없이 그냥 건너가게 될 수 있기 때문이다.
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # -1: 방문 안함 0: 방문함 1:굵은 선
    maps = [[-1 for _ in range(102)] for _ in range(102)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for r in rectangle:
        # 각 좌표를 2배 해준다. 최단 거리 이기 때문에 길을 잘 못 탐색하는 것을 방지.
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 직사각형 범위 안을 0으로 만들어준다.
                if x1 < i < x2 and y1 < j < y2:
                    maps[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리일 때 1로 채움
                elif maps[i][j] != 0:
                    maps[i][j] = 1

    def bfs(cx, cy):
        nonlocal answer
        dq = deque()
        maps[cx][cy] = 2
        dq.append([cx, cy])

        while dq:
            x, y = dq.popleft()
            if x == itemX * 2 and y == itemY * 2:
                answer = maps[x][y] // 2
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    dq.append([nx, ny])

    bfs(characterX * 2, characterY * 2)

    return answer - 1