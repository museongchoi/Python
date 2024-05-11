# 수들의 합 2
# n 개의 수들이 n[i] + n[i+1] + n[i+2] .. n[j] 까지 합이 m이 되는 경우의 수 구하기.
# 투 포인터 사용, 포인터를 이동시키며 포인터 범위의 총합이 특정 값에 도달하는 것을 검사 범위를 줄이면서 계산

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 1
cnt = 0

while right <= n and left <= right:
    #print(left, right)
    total = sum(nums[left:right])

    if total == m:
        cnt += 1
        right += 1
    elif total < m:
        right += 1
    elif total > m:
        left += 1

print(cnt)