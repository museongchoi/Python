# 팩토리얼 0의 개수

# 방법 1
n = int(input())
num = 1
for i in range(1, n+1):
    num *= i

cnt = 0
for j in str(num)[::-1]:
    if j != '0':
        break
    cnt += 1

print(cnt)