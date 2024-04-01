# A + B 출력
# 방법 3 : 48ms
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)

# 방법 2 : 40 ms
# import sys
#
# T = int(sys.stdin.readline())
# for _ in range(T):
#     print(sum(map(int, sys.stdin.readline().split())))


# 방법 1 : 48ms
# T = int(input())
# for _ in range(T):
#     print(sum(map(int, input().split())))