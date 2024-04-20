# 사분면 고르기
# 1 : 양/양, 2 : 음/양, 3 : 음/음, 4 : 양/음
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
