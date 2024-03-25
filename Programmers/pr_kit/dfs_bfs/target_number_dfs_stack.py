# stack 을 이용한 dfs
def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx):
        nonlocal answer
        q = [[numbers[0], 0], [-1 * numbers[0], 0]]

        while q:
            tmp, idx = q.pop()
            idx += 1
            if idx < n:
                q.append([tmp + numbers[idx], idx])
                q.append([tmp - numbers[idx], idx])
            else:
                if tmp == target:
                    answer += 1

    dfs(0)
    return answer