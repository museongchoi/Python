# 타겟 넘버 dfs
def solution(numbers, target):
    answer = 0
    n = len(numbers)

    # idx 를 이용한 numbers의 값 계산.
    # 계산한 결과를 저장할 result.
    def dfs(idx, result):
        # numbers 의 길이 n과 idx가 동일시 numbers의 마지막 값까지 계산한 결과 이므로 target과 같은지 비교.
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer