# 숫자의 합
# N개의 숫자가 입력이 붙어서 들어온다.
# list 형으로 입력 받는 방법
import sys
N = int(input())
numlist = list(map(int, sys.stdin.readline().strip()))
ans = 0
for i in range(N):
    ans += numlist[i]

print(ans)