# 연산자 끼워넣기
# 1. n : 숫자의 개수
# 2. n개의 숫자
# 3, 각 연산 횟수 +, -, *, %

# 풀이
# 1. 최대, 최소, 연산 실행한 값 저장 변수
# 2. 각 연산 횟수 저장 변수
# 3. 되돌아 왔을때 남아 있는 연산을 실행해야 한다.
# + - * % 연산이 1나씩 연산한다고 과정.
# 첫번째 연산 순서 + -> - -> * -> // 일때 -로 돌아감
# + -> - -> // -> * 연산후 -로 돌아감
# + -> * -> - -> // 끝까지 반복

import sys
input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_num = -1e9
min_num = 1e9

def DFS(dept, total, plus, minus, multiply, divide):
    global max_num, min_num
    if dept == n:
        max_num = max(max_num, total)
        min_num = min(min_num, total)

    if plus:
        DFS(dept + 1, total + num_list[dept], plus-1, minus, multiply, divide)
    if minus:
        DFS(dept + 1, total - num_list[dept], plus, minus-1, multiply, divide)
    if multiply:
        DFS(dept + 1, total * num_list[dept], plus, minus, multiply-1, divide)
    if divide:
        DFS(dept + 1, total // num_list[dept], plus, minus, multiply, divide-1)

DFS(1, num_list[0], oper[0], oper[1], oper[2], oper[3])
print(max_num)
print(min_num)