# 퇴사
# top down

# 재귀 사용
import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range((n+1))]
ans = 0
def find(day, s):
    global ans
    if day > n:
        return
    if day == n:
        ans = max(ans, s)
        return
    find(day+li[day][0], s+li[day][1])
    find(day+1, s)

find(0,0)
print(ans)
