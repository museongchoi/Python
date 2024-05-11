# 슬라이딩 윈도우 알고리즘 예시
# 배열안 5개의 최대핪을 구하라.

import sys
input = sys.stdin.readline
numbers = [1,3,2,6,-1,4,1,8,2]
n = len(numbers)
k = 5 # 묶음
window = sum(numbers[:k]) # 초기 묶음 합, numbers의 시작 범위 총 합
ans = window # 값을 비교하기 위한 초기 값을 지정, window 값을 저장

for i in range(k, n):
    window += numbers[i] - numbers[i-k]
    ans = max(ans, window) # max 함수를 사용, 최대값을 구한다

print(ans)