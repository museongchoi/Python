# 덱
from collections import deque
import sys

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    # 정수 x를 dq 앞에 넣는다.
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    # 정수 x를 dq 뒤에 넣는다.
    elif command[0] == 'push_back':
        dq.append(command[1])
    # dq의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    # dq의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    # dq에 들어 있는 정수의 개수
    elif command[0] == 'size':
        print(len(dq))
    # dq 가 비어있으면 1을, 아니면 0을 출력
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    # dq의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    # dq의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
