# 별찍기-4
N = int(input())

for i in range(N,0,-1):
    print(' '*(N-i) + '*'*i)