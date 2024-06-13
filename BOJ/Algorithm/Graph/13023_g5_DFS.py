# 코드 2
# ABCDE
n, m = map(int, input().split())

p_num = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    x, y = map(int, input().split())
    p_num[x].append(y)
    p_num[y].append(x)

def DFS(a, depth):
    global ans
    visited[a] = True
    # 입력값이 주어 졌을때, 깊이를 확인한다.
    if depth >= 4:
        ans = True
        return

    # 현재 위치에 이어져 있는 노드 즉, 친구를 확인한다.
    # 방문 하지 않았다면, 연결 노드와 깊이 + 1 를 DFS 입력값으로 주고 재귀 실행.
    for b in p_num[a]:
        if visited[b] == False:
            DFS(b, depth + 1)
    visited[a] = False


ans = False # 성공 여부
depth = 0

# 깊이와 현재 위치를 입력값으로 준다.
# 현재 위치에 깊이가 4 이상이면 통과
for i in range(n):
    DFS(i, depth)
    if ans == True:
        print(1)
        break
else:   # 위 반복문이 if 문에 걸리지 않고 정상적으로 마무리가 되면 해당 조건에 만족하는게 아니기 때문에 0을 출력.
    print(0)

#-----------
# 코드 1
# # ABCDE
# n, m = map(int, input().split())
#
# p_num = [[] for _ in range(n)]
# visited = [False] * n
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     p_num[x].append(y)
#     p_num[y].append(x)
#
# def DFS(a, depth):
#     global ans
#     # 입력값이 주어 졌을때, 깊이를 확인한다.
#     if depth >= 4:
#         ans = True
#         return
#     # 현재 위치에 이어져 있는 노드 즉, 친구를 확인한다.
#     # 방문 하지 않았다면, 연결 노드와 깊이 + 1 를 DFS 입력값으로 주고 재귀 실행.
#     for b in p_num[a]:
#         if visited[b] == False:
#             visited[b] = True
#             DFS(b, depth + 1)
#             visited[b] = False
#
#
# ans = False # 성공 여부
# depth = 0
#
# # 깊이와 현재 위치를 입력값으로 준다.
# # 현재 위치에 깊이가 4 이상이면 통과
# for i in range(n):
#     visited[i] = True
#     DFS(i, depth)
#     if ans == True:
#         print(1)
#         break
#     visited[i] = False
# else:   # 위 반복문이 if 문에 걸리지 않고 정상적으로 마무리가 되면 해당 조건에 만족하는게 아니기 때문에 0을 출력.
#     print(0)