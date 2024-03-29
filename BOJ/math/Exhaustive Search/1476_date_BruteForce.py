# 날짜 계산
# 1 <= 지구E <= 15, 1 <= 태양S <= 28, 1<= 달M <= 19
import sys
E, S, M = map(int, sys.stdin.readline().split())
year = 1
while True:
    if (year-E)%15 == 0 and (year-S)%28 == 0 and (year-M)%19 == 0:
        break
    year += 1

print(year)

# while 문 조건에 걸리면 출력
# import sys
# E, S, M = map(int, sys.stdin.readline().split())
#
# def date(cnt):
#     e, s, m = 1, 1, 1
#     while True:
#         e += 1
#         s += 1
#         m += 1
#         cnt += 1
#         if e > 15:
#             e = 1
#         if s > 28:
#             s = 1
#         if m > 19:
#             m = 1
#         if S == s:
#             if e == E and m == M:
#                 return cnt
#
# if E == 1 and S == 1 and M == 1:
#     print(1)
# else:
#     print(date(1))