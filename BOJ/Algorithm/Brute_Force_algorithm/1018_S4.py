# 체스판 다시 칠하기
# n*m 크기의 체스판, b : 검정 / w : 흰색
# 8*8 크기의 체스판을 잘라서 만든다. 이때 체스판을 수정하는데 필요한 최소 개수.
# 체스판은 처음 시작점이 b와 w로 시작하는 두가지 경우의 수만 존재.
# B로 시작 : 홀수가 W / 짝수가 B
# W로 시작 : 홀수가 B / 짝수가 W

# 검사 시작 범위 설정 : 8*8의 체스판이므로 원본 체스판이 넘지 않는 선에서 검사를 해야한다.
# 시작 범위를 기준으로 검사 시작. 검사 시작 범위 ~ +8까지 x,y축을 검사한다.
# 현재 검사하는 위치가 홀수, 짝수 인지 판별.
# 홀수, 짝수 일때 각각 B/W로 시작하는 경우의 수 두가지를 검사한다.

# 짝수
# B로 시작, 현재 위치가 짝수 일때 B가 아니면 cntB 증가
# W로 시작, 현재 위치가 짝수 일때 W가 아니면 cntW 증가

# 홀수
# B로 시작, 현재 위치가 홀수 일때 W가 아니면 cntB 증가
# W로 시작, 현재 위치가 홀수 일때 B가 아니면 cntW 증가

# 최종 변경 개수를 리스트에 저장, 아니면 최소값을 비교하는 방법으로 cnt를 세서 tmp에 저장.

# 방법 2 : 방법 1에 반복문 인덱스 접근 변경
import sys
n, m = map(int, input().split())
maps = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
tmp = 251

for i in range(n-7):
    for j in range(m-7):
        cntB = 0
        cntW = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if maps[x][y] != 'B':
                        cntB += 1
                    if maps[x][y] != 'W':
                        cntW += 1
                else:
                    if maps[x][y] != 'W':
                        cntB += 1
                    if maps[x][y] != 'B':
                        cntW += 1

        tmp = min(tmp, cntB, cntW)

print(tmp)


# 방법 1
# import sys
# n, m = map(int, input().split())
# maps = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
# tmp = 251
#
# for i in range(n-7):
#     for j in range(m-7):
#         cntB = 0
#         cntW = 0
#         for x in range(8):
#             for y in range(8):
#                 if (x+y) % 2 == 0:
#                     if maps[x+i][y+j] != 'B':
#                         cntB += 1
#                     if maps[x+i][y+j] != 'W':
#                         cntW += 1
#                 else:
#                     if maps[x+i][y+j] != 'W':
#                         cntB += 1
#                     if maps[x+i][y+j] != 'B':
#                         cntW += 1
#
#         tmp = min(tmp, cntB, cntW)
#
# print(tmp)