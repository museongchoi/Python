# 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())

dq = deque(i for i in range(1, n+1))
cnt = 0
ans = []
while dq:
    cnt += 1
    if cnt == k:
        ans.append(dq.popleft())
        cnt = 0
    else:
        dq.append(dq.popleft())

print('<' + ', '.join(str(i) for i in ans) + '>')