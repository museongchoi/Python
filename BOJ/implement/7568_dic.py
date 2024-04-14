# 덩치
import sys
n = int(input())
dic = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dic[x] = y

for p in dic:
    for 