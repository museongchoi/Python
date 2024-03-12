# 정수를 나선형으로 배치하기
def solution(n):
    if n == 1:
        return [[1]]

    answer = [[0 for _ in range(n)] for _ in range(n)]
    mode = 0  # 오른쪽 0, 아래 1, 왼쪽 2, 위 3
    x, y = 0, 0

    for i in range(n ** 2):
        answer[x][y] = i + 1
        if mode == 0:
            y += 1
            if y == n - 1 or answer[x][y + 1] != 0:
                mode = 1
        elif mode == 1:
            x += 1
            if x == n - 1 or answer[x + 1][y] != 0:
                mode = 2
        elif mode == 2:
            y -= 1
            if y == 0 or answer[x][y - 1] != 0:
                mode = 3
        elif mode == 3:
            x -= 1
            if x == 0 or answer[x - 1][y] != 0:
                mode = 0

    return answer