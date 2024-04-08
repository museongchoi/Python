# 별찍기-17

N = int(input())

for i in range(1, N+1):
    if i == 1 or i == N:
        print(' ' * (N-i) + '*' * ((i*2)-1))
    else:
        print(' ' * (N - i) + '*' + " " * ((i * 2) - 3) + '*')
