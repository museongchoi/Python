# 10952
# 마지막 입력은 a,b 가 0 0 이 들어온다.

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)