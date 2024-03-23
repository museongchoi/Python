from collections import deque
def solution(maps):
    answer = 0
    # 북0동1남2서3
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        dq = deque()
        dq.append([x, y])

        while dq:
            x, y = dq.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[x][y] + 1
                        dq.append([nx, ny])

        return maps[len(maps)-1][len(maps[0]) - 1]

    answer = bfs(0, 0)

    return -1 if answer == 1 else answer