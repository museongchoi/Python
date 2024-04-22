# 공바꾸기
# 총 바구니 n개, m번 공을 바꿈, i/j 번 바구니 공을 교환.
# 처음 바구니에는 바구니 번호와 같은 공 번호가 들어가 있다.

n, m = map(int, input().split())
basket = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]

for i in basket[1:]:
    print(i, end=' ')