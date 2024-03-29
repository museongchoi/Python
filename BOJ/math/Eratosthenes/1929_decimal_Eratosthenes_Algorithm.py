# 소수 구하기
M, N = map(int, input().split())
def get_prime(n):
    # 16 개 생성
    vi = [False, False] + [True] * (n - 1)
    ans = []
    # 2부터 N+1 까지 순회
    for i in range(2, n+1):
        # 숫자 i의 배수를 False 로 체크, 배수가 있으면 소수 이므로 다음 순회일때 걸리지 않을 것이다.
        if vi[i]:
            ans.append(i)
            for j in range(i*2, n+1, i):
                vi[j] = False

    return ans

primes = get_prime(N)

for num in primes:
    if num >= M:
        print(num)
