# 슬라이딩 윈도우 알고리즘 예시
# 배열안 5개의 최대핪을 구하라.

import sys
input = sys.stdin.readline
numbers = [1,3,2,6,-1,4,1,8,2]
n = len(numbers)
k = 5 # 묶음
window = sum(numbers[:k]) # 초기 묶음 합
ans = window

for i in range(k, n):
    window += numbers[i] - numbers[i-5]
    ans = max(ans, window)

print(ans)