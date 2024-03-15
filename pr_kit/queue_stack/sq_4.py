# 다리를 지나는 트럭

# 코드 설명
# 다리의 길이 만큼 0으로 채운다. 이는 다리에서 트럭을 전진 시키기 위해, 0으로 한 이유는 무게 확인을 위해
# 다리가 트럭 위에 올라가는 시점부터 시작이므로 cnt++
# sum 함수 대신 무게를 실시간으로 확인
# breidgeweight = 0 다리에서 빠져나가는 트럭의 무게를 빼야한다
# 다리 위에 올라가도 되는지 현재 다리위 무게와 기다리고 있는 첫번째 트럭 무게를 합한다
# breidgeweight += truck.popleft() 다리위에 올라가는 트럭 무게를 더한다
# 다리 위에 트럭이 올라가지 못한다면 0을 추가하여 트럭을 전진 시킨다
# 트럭이 다리 위에 다 올라갔다면 트럭이 다리를 빠져나가야 하므로 현재 다리 길이 len(bridge) 를 cnt 에 더한다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)

    breidgeweight = 0
    while len(truck) != 0:
        cnt += 1
        breidgeweight -= bridge.popleft()

        if breidgeweight + truck[0] <= weight:
            el = truck.popleft()
            breidgeweight += el
            bridge.append(el)
        else:
            bridge.append(0)

    cnt += len(bridge)

    return cnt
