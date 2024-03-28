# 스택
#이때, input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다.
#입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
import sys

N = int(sys.stdin.readline())
st = []

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        st.append(command[1])
    elif command[0] == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    elif command[0] == 'size':
        print(len(st))
    elif command[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])



# from collections import deque
# import sys
#
# N = int(sys.stdin.readline())
# st = deque()
#
# for _ in range(N):
#     command = sys.stdin.readline().split()
#
#     if command[0] == 'push':
#         st.append(command[1])
#     elif command[0] == 'pop':
#         if len(st) == 0:
#             print(-1)
#         else:
#             print(st.pop())
#     elif command[0] == 'size':
#         print(len(st))
#     elif command[0] == 'empty':
#         if len(st) == 0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'top':
#         if len(st) == 0:
#             print(-1)
#         else:
#             print(st[-1])
