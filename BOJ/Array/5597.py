# 과제 안 내신 분..?
# 30 명의 학생 중 2명이 과제를 제출하지 않음. 두명의 학생을 구하기.
visited = [0 for _ in range(31)]
visited[0] = 1
for _ in range(28):
    n = int(input())
    visited[n] = 1

for i in range(len(visited)):
    if visited[i] == 0:
        print(i)