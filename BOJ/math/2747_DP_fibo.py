# 피보나치 수
#topdown
N = int(input())
dp = [0] * (N+1)

def find(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = find(x-1) + find(x-2)

    return dp[x]

print(find(N))

# bottom up
# N = int(input())
# dp = [0] * (N+1)
#
# dp[0] = 0
# dp[1] = 1
#
# for i in range(2, N+1):
#    dp[i] = dp[i-1] + dp[i-2]
#
# print(dp[N])