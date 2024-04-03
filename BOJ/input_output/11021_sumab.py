# "Case #x: "를 출력한 다음, A+B를 출력한다
import sys

T = int(input())

for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}:', A+B)