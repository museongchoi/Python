# 바구니 뒤집기
# 바구니 n개 (1~n), m 번 바구니의 순서를 역순으로 바꾼다.
# i/j : i번째 바구니부터 j번째 바구니의 순서를 역순으로 만듬.
n, m = map(int, input().split())
basket = [k for k in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    # idx가 하나씩 밀려 있으므로 i-1, j-1을 해야한다.
    tmp = basket[i-1:j]
    # 리스트 요소를 역순으로 재배열.
    tmp.reverse()
    # 리스트는 변경 가능한 자료형이기 때문에 슬라이싱을 사용하여 요소 변경.
    basket[i-1:j] = tmp

for k in range(n):
    print(basket[k], end=' ')