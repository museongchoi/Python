# 진법 변환
# 0123456789ABCDEFGHIZKLMNOPQRSTUVWXYZ
ten = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
b = int(b)

ans = 0

for i in range(len(n)-1,-1,-1):
    # n[len(n)-1-i] 는 현재 반복문이 역으로 순회중 이지만 n의 첫번째 값을 구해야하기 때문에 길이의 -1에 i를 빼주면 0~끝까지 문자를 가지고 온다.

    s = ten.index(n[len(n)-1-i]) * (b**i)
    ans += s

print(ans)