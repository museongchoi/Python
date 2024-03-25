def solution(maps):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y):

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return maps[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    dfs(nx, ny)

    # 0 : 벽, 1 : 벽이 없는 자리
    answer = dfs(0, 0)
    return answer