# 수들의 합 2
# n 개의 수들이 n[i] + n[i+1] + n[i+2] .. n[j] 까지 합이 m이 되는 경우의 수 구하기.
# 슬라이싱 윈도우 개념으로 중 복되는 구간 제외 앞, 뒤를 더하고 빼면서 계산 한다.
# 시간 초과 발생

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0 # 경우의 수

# 묶음을 2부터 늘려나간다.
for k in range(1, n+1):
    window = sum(li[:k])
    if window == m:
        cnt += 1
    for i in range(k, n):
        window += li[i] - li[i-k]
        if window == m:
            cnt += 1

print(cnt)
