# 공 넣기
# n : 총 바구니 개수, m : 공 넣는 횟수, i/j : 바구니 번호, k : 공 번호
# i~j번 바구니에 k번 공을 넣는다. 바구니에 공이 있을 경우 빼고 넣는다. 마지막 바구니에 들어있는 공 번호를 출력, 빈 곳은 0으로 출력.
n, m = map(int, input().split())
basket = [0 for _ in range(n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for s in range(i, j+1):
        basket[s] = k

for s in range(1, len(basket)):
    print(basket[s], end=' ')