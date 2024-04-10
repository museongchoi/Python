# 색종이
# 단순하게 중복된 도화지의 영역을 생각하지 말자
# 검은 도화지의 영역을 1로 체크하여 전체 흰도화지 범위를 돌면서 값이 1인 요소의 개수를 센다.
n = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            cnt += 1
# count 함수 사용. h 행에 값이 1인 요소의 개수를 반환
# for h in range(101):
#    cnt += paper[h].count(1)
print(cnt)

# 방법 1
# N = int(input())
# array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화
# for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
#     y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.
#
#     for i in range(x1, x1 + 10):  # 세로를 돈다.
#         for j in range(y1, y1 + 10):  # 가로를 돈다.
#             array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.
#
# count 함수를 사용하여 k번째 행에 값이 1인 요소의 개수를 반환.
# result = 0  # 넓이를 출력할 변수
# for k in range(100):  # 전체 도화지를 돌면서
#     result += array[k].count(1)  # 1 개수만 세어준다
#
# print(result)