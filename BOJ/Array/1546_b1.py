# 평균
# 시험본 과목 개수 n
import sys
n = int(input())
num = list(map(int, sys.stdin.readline().split()))
m = max(num)
snum = 0

for k in num:
    snum += k/m*100

print(snum/n)
