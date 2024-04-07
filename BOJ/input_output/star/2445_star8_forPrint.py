# 별찍기-8
N = int(input())

for i in range(1, 2*N):
    if i <= N:
        print("*" * i + " " * ((N-i)*2) + "*" * i)
    else:
        print("*" * (N-(i-N)) + " " * ((i-N)*2) + "*" * (N-(i-N)))

# 방법 1
# n = int(input())
# for i in range(1,n+1):
#     print("*" * i + " " * 2*(n-i) + "*" * i)
# for j in range(1,n):
#     print("*"* (n-j) + " " * 2*j + "*" * (n-j))