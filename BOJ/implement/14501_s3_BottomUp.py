# 퇴사
# bottom up
import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for day in range(n):
    for j in range(day+li[day][0], n+1):
        if dp[j] < dp[day] + li[day][1]:
            dp[j] = dp[day] + li[day][1]

print(dp)
print(dp[-1]) # 최종 가장 마지막 값 출력
