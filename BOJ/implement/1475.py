# 방 번호
# 입력 받은 숫자를 순회. 각 숫자를 visited 방문체크를 한다.
# 방문 체크를 한번만 하는 것이 아닌 몇번을 방문 했는지 해당 idx에 체크한다.
# 최대 방문 횟수를 출력.
n = input()
visited = [0 for i in range(10)]

# 6, 9 조건, 6 이나 9 일때 작은 값을 증가 시키기. 작은 값이 없으면 해당 값 증가
for k in n:
    k = int(k)
    if k == 6 or k == 9:
        if visited[6] < visited[9]:
            visited[6] += 1
        elif visited[6] > visited[9]:
            visited[9] += 1
        else:
            visited[k] += 1
    else:
        visited[k] += 1

print(max(visited))