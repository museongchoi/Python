import math
M, N = map(int, input().split())
def is_prime(x):
    # 1은 소수가 아니므로 False
    if x <= 1:
        return False
    # math 모듈의 sqrt 함수를 사용 2 부터 제곱근의 + 1까지 숫자를 해당 숫자 x와 나누어 나머지가 0이 되면 소수 False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    # 위 조건이 아니면 True
    return True

# M 부터 N 까지 순회, is_prime 함수에서 소수가 아니면 True를 맞으면 False 반환
for num in range(M, N+1):
    if is_prime(num):
        print(num)
