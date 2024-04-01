# A + B 를 출력
# 테스트 케이스가 몇개가 들어올지 미정

import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break

# import sys
#
# while True:
#     try:
#         print(sum(map(int, sys.stdin.readline().split())))
#     except:
#         break