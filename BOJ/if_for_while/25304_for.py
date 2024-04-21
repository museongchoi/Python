# 영수증
# x : 총 금액, n : 구매 물건 총 개수, a/b : 가격/개수
# 1. 입력 받기
# 2. 최종 계산 금액과 x 비교

x = int(input())
n = int(input())

val = 0
for _ in range(n):
    a, b = map(int, input().split())
    val += a*b

if x == val:
    print('Yes')
else:
    print('No')