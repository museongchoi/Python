# 벌집
# 1번 방부터 시작하여 n벙 방으로 도착하는 최단 거리를 구하는 것.
# 주의할점은 최단거리라고 특정 막힘 구간이 있는것이 아닌 일자로 이동 가능 하므로 그래프는 아니다.
# 방 개수 1번째 : 1번/1개, 2번째 : 2번~7번/6개, 3번째 : 8번~19번/12개
# 다음 가장자리(cnt)는 6개씩 방이 증가한다. box + (6*cnt)
n = int(input())
room = 1
cnt = 1

while n > room:
    room += 6*cnt
    cnt += 1

print(cnt)
