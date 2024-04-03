# A + B 를 출력
# 테스트 케이스가 몇개가 들어올지 미정
# A,B에 입력값이 들어온 try 일때 출력 진행, 입력값이 들어오지 않으면 break
# 이 코드는 입력된 두 숫자 A와 B를 분리하여 각각 변수에 할당한 후, 이들의 합을 출력합니다.
# 입력이 올바르지 않거나 EOF에 도달하면 except 블록이 실행되어 반복문이 종료됩니다.

import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break

# import sys
#
# while True:
#     try:
#         print(sum(map(int, sys.stdin.readline().split())))
#     except:
#         break