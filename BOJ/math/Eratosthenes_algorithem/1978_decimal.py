# 소수 찾기
# 방법 2
# import sys
# n = int(input())
# deci = list(map(int, sys.stdin.readline().split()))
# cnt = 0
#
# for i in deci:
#     if i == 1:
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     # while 문에에서 else를 단독으로 사용하면 중간에 break문에 걸리지 않고 다 돌아갈 경우 진행 된다.
#     else:
#         cnt += 1
# print(cnt)


# 방법 1
# 에라토스테네스의 체 알고라즘은 소수를 빠르게 찾는 알고리즘
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))

# True : 소수, False : 비소수
# vi : x까지
def get_prime(x):
    vi = [False, False] + [True] * (x-1)
    for i in range(2, x+1):
        if vi[i]:
            for j in range(i**2, x+1, i):
                vi[j] = False
    return vi

x = max(a)
pvi = get_prime(x)
cnt = 0
for num in a:
    if pvi[num]:
        cnt += 1

print(cnt)
