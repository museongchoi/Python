# 완전제곱수의 합
N = int(input())
dp = [i for i in range(N+1)]

for i in range(2, N+1):
    for j in range(1, N+1):
        square = j**2
        # 각 제곱수가 i 입력값을 넘으면 break
        if i < square:
            break
        # 각 제곱수 사용하여 만들수 있는 항의 개수를 구한다.
        # 반복문을 사용하여 입력값 i 를 넘지 않는 j의 제곱수 square를 i에서 뺀 후 + 1 한 값이,
        # 해당 제곱수를 사용하여 만들수 있는 항의 개수이다. 이 중 가장 작은 값을 찾는다.
        if dp[i] > dp[i-square] + 1:
            dp[i] = dp[i-square] + 1

print(dp[N])
