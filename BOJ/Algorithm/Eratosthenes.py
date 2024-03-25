n=1000
# a 는 0, 1 자리 False, 나머지는 True
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)    # True 일때만 추가. 즉, 소수 일때만 추가
    for j in range(2*i, n+1, i):    # 자기 자신의 배수를 지우는 과정
        a[j] = False
print(primes)