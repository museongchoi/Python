# 콤마를 기준으로 입력이 들어온다
import sys
T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split(','))
    print(A+B)
