# 최소, 최대
# 방법 2가 가장 빠름

# 방법 5
import sys
N = int(input())
mlist = list(map(int, sys.stdin.readline().split()))
minn = 1000000
maxn = -1000000
for i in mlist:
    if minn > i:
        minn = i
    if maxn < i:
        maxn = i
print(minn, maxn)
# sort 사용
#mlist.sort()
#print(mlist[0], mlist[-1])

# 방법 4
# N = int(input())
# m_list = list(map(int, input().split()))
# minn = 1000000
# maxn = -1000000
# for i in m_list:
#     if int(i) < minn:
#         minn = i
#     if int(i) > maxn:
#         maxn = i
# print(minn, maxn)

# 방법1. sort, slicing 사용
# N = int(input())
# m_list = list(map(int, input().split()))
# m_list.sort()
# print(m_list[0], m_list[-1])

# 방법2. min, max 함수 사용
# N = int(input())
# m_list = list(map(int, input().split()))
#
# ans1 = min(m_list)
# ans2 = max(m_list)
#
# print(ans1, ans2)

# 방법3. 리스트 사용
# N = int(input())
# m_list = list(map(int, input().split()))
# ans = []
# ans.append(min(m_list))
# ans.append(max(m_list))
#
# for i in ans:
#     print(i, end=' ')
