# 수들의 합 2
# n 개의 수들이 n[i] + n[i+1] + n[i+2] .. n[j] 까지 합이 m이 되는 경우의 수 구하기.
# 투 포인터 사용, 포인터를 이동시키며 포인터 범위의 총합이 특정 값에 도달하는 것을 검사 범위를 줄이면서 계산

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 1 # 포인터 지정
cnt = 0 # 경우의 수, 포인터의 범위 합 == m 일때 cnt 증가

while right <= n and left <= right:
    #print(left, right)
    total = sum(nums[left:right]) # nums 리스트의 포인터 범위 합을 total에 저장

    # total 값을 3가지 조건으로 나누어 비교
    if total == m:  # 1. total 값이 m과 같을 때 경우의 수를 구하는 것.
        cnt += 1
        right += 1
    elif total < m: # total 값이 m 보다 작으면 값이 부족하므로 right 포인터를 증가 시켜 total 값에 더해준다.
        right += 1
    elif total > m: # total 값이 m 보다 크면 left 포인터를 증가 시켜 앞에 + 했던 값을 빼준다.
        left += 1

print(cnt)