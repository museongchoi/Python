# 중앙 이동 알고리즘
# 방법 1
n = int(input())
cnt = 2
for i in range(1, n+1):
    cnt += (cnt - 1)

print(cnt**2)

# 방법 2
# (2^n + 1)^2 규칙
#print((2**int(input())+1)**2)

# 방법 3
# 1+2**n 규칙