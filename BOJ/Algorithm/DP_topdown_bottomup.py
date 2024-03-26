# topdown
# 한 번 계산된 결과를 메모이제이하기 위한 리스트 초기화
dp = [0] * 100

# 피보나치 함수 (Fibonacci Function)를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건 : 1 or 2 일때 1을 반환
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과를 반환
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo(99))

#bottomup
# 앞서 계산한 결과를 저장하기 위한 dp 리스트 초기화 선언
d = [0] * 100
# 첫번째, 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

for idx in range(3, n+1):
    d[idx] = d[idx-1] + d[idx-2]

print(d[n])