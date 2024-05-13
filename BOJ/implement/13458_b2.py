# 시험 감독
# b : 총 감독관 감독 가능 인원수, c : 부 감독관 감독 가능 인원 수
import sys
input = sys.stdin.readline

n = int(input())
test_num = list(map(int, input().split()))
b, c = map(int, input().split())
# 총 감독관은 최소 1명이 각 시험장에 있어야 한다.
# 각 시험장 마다 있는 감독관 최소 수를 구하라.
cnt = 0
for test in test_num:
    cnt += 1
    test -= b

    if test > 0:
        if test%c == 0:
            cnt += test//c
        else:
            cnt += test//c + 1

print(cnt)