# 주사위 세개
# a, b, c 입력 받기
# 방법 2
a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b or a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(max(a, b, c)*100)

# # 방법 1
# # dice 리스트로 입력을 받고, 주사위 방문 리스트 생성.
# # dice 순회 vidice에 방문 체크
# import sys
# dice = list(map(int, sys.stdin.readline().split()))
# vidice = [0 for _ in range(6+1)]
#
# for i in dice:
#     vidice[i] += 1
#
# # vidice 의 가장 큰 값을 조건 3 or 2 를 비교한뒤 없으면 3 주사위 값이 다 다른것이므로 dice의 가장 큰 수를 계산
# vi = max(vidice)
# if vi == 3:
#     print(10000 + vidice.index(vi) * 1000)
# elif vi == 2:
#     print(1000 + vidice.index(vi) * 100)
# else:
#     print(max(dice) * 100)

