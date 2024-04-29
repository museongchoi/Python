# 수학은 비대면 강의 입니다.
# a,b,c,d,e,f 를 방정식에 대입하여 만족하는 x, y 값을 출력
# 방정식 : ax + by = c / dx + ey = f
# -999 <= x, y <= 999
# 방법 3
import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())


# 방법 2 - 브루트포스 알고리즘
# import sys
# a, b, c, d, e, f = map(int, sys.stdin.readline().split())
# for i in range(-999, 1000):
#     for j in range(-999, 1000):
#         if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
#             print(i, j)

# 방법 1
# import sys
# a,b,c,d,e,f = map(int, sys.stdin.readline().split())
# # a와 d를 서로 곱함. b,c 에 d를 곱하기 / e,f 에 a를 곱하기
# # (b - e)y = c - f => c-f // b-e = y 값을 구한다.
# # ax + by = c 식에 y를 대입하여 x 를 구한다. c-b*y = x
#
# bd = b*d
# cd = c*d
# ea = e*a
# fa = f*a
# y = (cd-fa)//(bd-ea)
# x = (c-(b*y))//a
# print(x, y)



