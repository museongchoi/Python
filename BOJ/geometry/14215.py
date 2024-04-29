# 세막대
# 가장 긴 길이 >= 나머지 막대 2개의 길이 합 : 삼각형이 아니다,
# 방법 2
alist = sorted(map(int, input().split()))
print(alist[0] + alist[1] + min(alist[2], alist[0]+alist[1]-1))

# 방법 1
# alist = list(map(int, input().split()))
#
# alist.sort()
# tmp = alist[0] + alist[1]
#
# if tmp <= alist[2]:
#     tmp += tmp-1
#     print(tmp)
# else:
#     print(sum(alist))
