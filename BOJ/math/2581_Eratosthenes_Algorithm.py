# 소수
M = int(input())
N = int(input())
def get_prime(n):
    vi = [False, False] + [True]*(n-1)
    ans = []

    for i in range(2, n+1):
        if vi[i]:
            ans.append(i)
            for j in range(i*2, n+1, i):
                vi[j] = False
    return ans

primes = get_prime(N)

tmp2 = 10001
tmp1 = 0
for num in primes:
    if num >= M:
        tmp1 += num
        if tmp2 > num:
            tmp2 = num

if tmp1 == 0:
    print(-1)
else:
    print(tmp1)
    print(tmp2)
