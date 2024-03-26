# A, B = [], []
#
# N, M = map(int, input().split())
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)
# print(A)
# print(B)
#[[1, 1, 1], [2, 2, 2], [0, 1, 0]]
#[[3, 3, 3], [4, 4, 4], [5, 5, 100]]

N, M = map(int, input().split())
ans = [[0]*M for _ in range(N)]
maps1 = [list(map(int, input().split())) for _ in range(N)]
maps2 = [list(map(int, input().split())) for _ in range(N)]
print(maps1)
print(maps2)
#[1, 1, 1], [2, 2, 2], [0, 1, 0]]
#[[3, 3, 3], [4, 4, 4], [5, 5, 100]]

for i in range(N):
    for j in range(M):
        ans[i][j] += maps1[i][j]
        ans[i][j] += maps2[i][j]
        print(ans[i][j], end=' ')
    print()
