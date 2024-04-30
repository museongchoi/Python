# 설탕 배달
# 3키로 5키로 설탕 봉지를 사용하여 n킬로 그램을 채우는 최소 개수.
# n킬로를 만들수 없다면 -1 출력
# 최대한 많은 양을 5키로로 채운고 3키로를 적게 사용한다.

# 방법 1
# n = int(input())
# bag = 0
#
# while n >= 0:
#     if n%5 == 0:
#        bag += n//5
#        print(bag)
#        break
#     n -= 3
#     bag += 1
# # for, while 문이 특정 조건에 걸리지 않고 끝까지 진행되면 실행되는 else 문 사용
# else:
#     print(-1)

# 방법 2
# 5로 나누어 떨어질 때
# 최소 3, 최대 5 사용
# 3으로 나누어 떨어질 때
# 나누어 떨어지지 않을 떄

n = int(input())
cnt = 0
if n%5 == 0:
    print(n//5)
else:
    cnt = 0
    while n > 0:
        n -= 3
        cnt += 1
        if n%5 == 0:
            cnt += n//5
            print(cnt)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(cnt)
            break

