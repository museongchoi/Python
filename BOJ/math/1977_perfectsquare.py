# 완전제곱수
# i의 제곱이 M <= i**2 <= N 의 범위에 속하고, 그 중 가장 작은 값과 범위 안에 값의 총합
M = int(input())
N = int(input())
snum = 0
mnum = N+1

for i in range(N):
    tmp = i*i
    if M <= tmp <= N:
        snum += tmp
        mnum = min(mnum, tmp)
    if tmp > N:
        break
# 총 합이 0 이라면 범위에 속하는 값이 없는 것. -1을 출력한다.
if snum == 0:
    print(-1)
else:
    print(snum)
    print(mnum)
