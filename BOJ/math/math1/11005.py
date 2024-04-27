# 진접 변환 2
n, b = map(int, input().split())
ten = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = ''
while n:
    a += str(ten[n%b])
    n //= b

print(a[::-1])
