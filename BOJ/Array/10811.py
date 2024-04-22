# 바구니 뒤집기
# 바구니 n개 (1~n), m 번 바구니의 순서를 역순으로 바꾼다.
# i/j : i번째 바구니부터 j번째 바구니의 순서를 역순으로 만듬.
n, m = map(int, input().split())
basket = [k for k in range(1, n+1)]
print(basket)
print(basket[1])

for _ in range(m):
    i, j = map(int, input().split())
    tmp = basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] = tmp

for k in range(n):
    print(basket[k], end=' ')



