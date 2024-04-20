# 오븐 시계
# 현재 시간 a, b / 요리하는 데 필요한 시간 c

a, b = map(int, input().split())
c = int(input())

tmp = b + c
# b + c 가 60 이상이면 a 증가.
# a에 더하는 값은 60으로 나는 몫
if tmp >= 60:
    tb = tmp%60
    a += tmp//60
    if a >= 24:
        a -= 24
    print(a, tb)
else:
    print(a, tmp)