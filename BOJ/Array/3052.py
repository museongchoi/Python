# 나머지
# 10개의 숫자를 42로 나눈 나머지의 서로 다른 값이 몇개 있는지 센다.
num = []
for _ in range(10):
    n = int(input())
    if n%42 not in num:
        num.append(n%42)

print(len(num))

