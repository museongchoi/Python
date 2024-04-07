# 별찍기-5
# 방법 2
# * 개수는 2의 배수 -1개 이다.
N = int(input())

for i in range(1, N+1):
    print(' '*(N-i) + '*'*(2*i-1))

# 방법 1
#N = int(input())

# for i in range(1, N+1):
#     if i == 1:
#         print(" " * (N - i) + '*' * i)
#     else:
#         print(" " * (N - i) + "*" * i + '*' * (i-1))
