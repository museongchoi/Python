# num = 1
# while num <= 100:
#     print(num)
#     num += 1

# 문제 1
#input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
#단, while 문을 사용하세요.

# num = int(input("반복 값&횟수 : "))
# cnt = 1
# while cnt <= num:
#     print(num)
#     cnt += 1

# 문제 2
#정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.1
import math

# num = int(input("num : "))
# cnt = 1
# while cnt <= num:
#     print(cnt, cnt*cnt)
#     cnt+=1

# 문제 3
#고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다.
#공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.

# tmp = 100
# h = 0.6
# maxcnt = 10
# cnt = 1
#
# while cnt <= maxcnt:
#     tmp = tmp * h
#     print(round(tmp, 4))
#     cnt+=1

#실행 결과를 맞추시오
#853
number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)
