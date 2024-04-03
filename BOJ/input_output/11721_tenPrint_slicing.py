# 10개씩 끊어서 출력하기
n = input()

for i in range(0, len(n), 10):
    print(n[i:i+10])

# #st = list(input().strip())
# st = list(input())
# ans = ''
# cnt = 0
# while len(st) != cnt:
#     ans += st[cnt]
#     cnt += 1
#     if cnt%10 == 0:
#         print(ans)
#         ans = ''
#
# print(ans)