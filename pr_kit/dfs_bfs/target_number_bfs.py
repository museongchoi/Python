# 타켓 넘버 bfs
from collections import deque
def solution(numbers, target):
    answer = 0

    def bfs(idx):
        nonlocal answer
        n = len(numbers)
        dq = deque()
        dq.append([numbers[idx], idx])
        dq.append([-1 * numbers[idx], idx])

        while dq:
            tmp, idx = dq.popleft()
            idx += 1
            if idx < n:
                dq.append([tmp + numbers[idx], idx])
                dq.append([tmp - numbers[idx], idx])
            else:  # idx > n 즉, n의 범위를 넘어간 마지막 값들이 popleft() 되어 xtmp 에 저장
                if tmp == target:
                    answer += 1

    bfs(0)

    return answer