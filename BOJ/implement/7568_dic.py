# 덩치
import sys
n = int(input())
dic = {}
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dic[x] = y

dic_s = sorted(dic.items())

for i in range(n):
    k = dic_s[i][0]
    v1 = dic_s[i][1]

    cnt = 0
    for j in range(i, n):
        v2 = dic_s[j][1]
        if v1 < v2:
            cnt += 1

    dic[k] = cnt + 1

print(list(dic.values()))