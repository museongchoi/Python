# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
import sys
T = int(input())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A} + {B} =", A+B)