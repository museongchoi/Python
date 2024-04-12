# 스택 수열
n = int(input())
mlist = []
for _ in range(n):
    mlist.append(int(input()))

order =[]
s = []
idx = 0
for i in range(1, n+1):
    s.append(i)
    order.append('+')
    while s:
        if s[-1] == mlist[idx]:
            s.pop()
            order.append('-')
            idx += 1
        else:
            break

if len(s) != 0:
    print('NO')
else:
    for i in order:
        print(i)