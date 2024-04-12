# 회전하는 큐
import sys
from collections import deque
#n, m = map(int, input().split())
n, m = map(int, sys.stdin.readline().split())
ch = list(map(int, sys.stdin.readline().split()))
# 1 ~ n 까지 dq를 생성
dq = deque([i for i in range(1, n+1)])
cnt = 0

# ch에 입력 받은 정수는 dq에서 뽑아내는 원소의 위치를 가르킨다.
# dq에서 1번 연산을 사용하여 해당 원소를 뽑아야 하는데, 이때 2,3번의 연산 횟수 최소값을 구한다.
for i in ch:    # dq[0]이 i일때 1번 연산을 하게된다.
    while True:
        if i == dq[0]:  # 1번 연산을 하게 되면 멈춤.
            dq.popleft()
            break
        # dp[0] == i 가 될때까지 구하는 과정. 이때 가까운 쪽으로 연산을 해야 한다.
        # idx를 활용 하여 구함. 
        # 현재 dq에 i의 idx를 구함.
        # 현재 dq의 길이를 2로 나눈 값과 i의 idx와 비교.
        else:
            # 2번 연산, 왼쪽으로 이동, 첫번째 값을 pop 오른쪽에 추가
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            # 3번 연산, 오른쪽으로 이동, 마지막 값을 pop 왼쪽에 추가
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)
