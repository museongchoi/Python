# 오븐 시계
# 현재 시간 a, b / 요리하는 데 필요한 시간 c

a, b = map(int, input().split())
c = int(input())

tmp = b + c

if tmp >= 60:
    # tmp%60 나머지가 분, 몫은 시간에 더한다.
    tb = tmp%60
    a += tmp//60
    if a >= 24:
        a =
        print(a, tb)
    else:
        print(a, tb)
else:
    print(a, tmp)