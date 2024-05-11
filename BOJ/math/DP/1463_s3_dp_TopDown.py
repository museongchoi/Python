# 1로 만들기
# Top Down / 재귀 사용

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
def find(idx):
    global dp
    # 1일때 계산 횟수는 0번, 0을 반환.
    if idx == 1:
        return 0
    if dp[idx] != 0:
        return dp[idx]

    # 2와 3으로 나누어 떨어질때, + 1을 하는 이유는 연산을 한번 한 것이므로, 1을 더해준다.
    if idx % 2 == 0 and idx % 3 == 0:
        dp[idx] = min(find(idx//2) + 1, find(idx//3) + 1)
    elif idx % 2 == 0:
        dp[idx] = min(find(idx//2) + 1, find(idx-1) + 1)
    elif idx % 3 == 0:
        dp[idx] = min(find(idx//3) + 1, find(idx-1) + 1)
    else:
        dp[idx] = find(idx-1) + 1

    return dp[idx]


print(find(n))