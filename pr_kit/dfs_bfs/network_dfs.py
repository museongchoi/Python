def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(idx):
        visited[idx] = True

        for k in range(n):
            if computers[idx][k] == 1 and visited[k] == False:
                dfs(k)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer