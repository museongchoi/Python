# 진접 변환 2
n, b = map(int, input().split())
ten = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 리스트가 아닌 문자열로 출력값을 저장.
a = ''
while n:
    a += str(ten[n%b])
    n //= b

# 슬라이싱을 이용하여 역순으로 출력.
print(a[::-1])
