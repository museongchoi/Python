# 1로 만들기

# # bottom up 알고리즘
# N = int(input())
# dp = [0] * (N+1)
# # print(dp)
#
# # 현재 숫자가 되기 위한 계산 횟수 중 가장 작은 횟수를 구한다.
# # 현재 숫자가 되기 위한 조건은 3가지 -1, //2, //3
# for i in range(2,N+1):
#     # i-1 의 계산 횟수를 d[i] 에 저장, 현재 계산 횟수보다 작은 계산 횟수를 찾아야한다.
#     # 1 빼기는 무조건 진행되는 조건이다. 이유는 2와 3으로 나누어 떯어진다는 조건이 있고, 빼기 1은 아무 조건이 없다.
#     dp[i] = dp[i-1] + 1
#     # 2 로 나누어 떨어지는 경우, 현재 계산 횟수와 (dp[i//2]계산횟수 + 1) 을 비교하여 작은 계산 횟수를 저장
#     if i%2 == 0:
#         dp[i] = min(dp[i], dp[i//2]+1)
#     # 3 으로 나누어 떨어지는 경우, 현재 계산 횟수와 (dp[i//2]계산횟수 + 1) 을 비교하여 작은 계산 횟수를 저장
#     if i%3 == 0:
#         dp[i] = min(dp[i], dp[i//3]+1)
#
# print('bottomup :', dp[N])

# topdown
N = int(input())
dp = [0] * (N+1)

def find(x):
    global dp
    print(dp)
    if x == 1:
        return 0
    if dp[x] != 0:
        return dp[x]
    if x%2==0 and x%3==0:
        dp[x] = min(find(x//3)+1, find(x//2)+1)
    elif x%3 == 0:
        dp[x] = min(find(x//3)+1, find(x-1)+1)
    elif x%2 == 0:
        dp[x] = min(find(x//2)+1, find(x-1)+1)
    else:
        dp[x] = find(x-1)+1

    return dp[x]

print(find(N))

