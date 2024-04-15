# 수강신청
import sys
k, l = map(int, sys.stdin.readline().split())
ans = []

for i in range(l):
    tmp = int(sys.stdin.readline())
    if tmp in ans:
        ans.remove(tmp)
    ans.append(tmp)

for j in range(k):
    print(ans[j])