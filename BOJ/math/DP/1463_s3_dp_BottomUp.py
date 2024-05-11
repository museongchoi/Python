# 1로 만들기
# bottom up / 반복문 사용

import sys
input = sys.stdin.readline

n = int(input())
# idx 가 1이 되기 위한 계산 횟수를 요소로 저장. 즉 idx는 n과 같다.
dp = [0] * (n+1)

# 1을 뺀 연산 횟수와 나누어 떨어진 연산 횟수를 비교한다. 더 연산 횟수가 적은 것을 idx의 연산 횟수 즉, 요소로 저장
for idx in range(2,n+1):
    # 1을 뺀다. idx에서 1을 뺀 값의 연산 횟수를 불러와 연산을 한번 계산한 것이므로 1을 더한다.
    dp[idx] = dp[idx-1] + 1
    # n 이 2로 나누어 떨어질때, 2로 나눈다. idx에서 2로 나눈 값의 연산 횟수를 불러와 한번 계산 한 것이므로 1을 더한다.
    if idx % 2 == 0:
        dp[idx] = min(dp[idx], dp[idx//2] + 1)
    # n 이 3으로 나누어 떨어질때, 3으로 나눈다
    if idx % 3 == 0:
        dp[idx] = min(dp[idx], dp[idx//3] + 1)

print(dp[n])