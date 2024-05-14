# 퇴사
# n+1 되는 날 퇴사.
# n일 동안 많은 상담을 진행. li는 상담을 완료하는 기간과 금액 입력, 상담이 완료 되기 전까지는 다른 상담 진행 불가.
# bottom up

import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for day in range(n):
    for j in range(day+li[day][0], n+1):
        if dp[j] < dp[day] + li[day][1]:
            dp[j] = dp[day] + li[day][1]

print(dp[-1])
