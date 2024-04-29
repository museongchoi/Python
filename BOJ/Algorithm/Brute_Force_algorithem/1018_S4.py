# 체스판 다시 칠하기
# n*m 크기의 체스판, b : 검정 / w : 흰색
# 8*8 크기의 체스판으로 잘라내어 수정할수 있다. 수정하는데 필요한 최소 정사각형 개수.
import sys
n, m = map(int, input().split())
maps = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
