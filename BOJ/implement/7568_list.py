# 덩치
# x 몸무게, y 키
# 자신보다 덩치가 큰 사람을 k명이라고 하면, 덩치 등수는 k+1.
# 키 x, p / 몸무게 y, q 가 있을때 x > p / y < q 는 덩치가 크다고 작다고 할 수 없다.
# 둘다 커야지 덩치가 큰 것.
import sys
n = int(input())
list_d = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    list_d.append([x, y])

# 리스트에 저장된 값 키를 비교한 뒤 몸무게 비교 후 둘다 통과이면 cnt 증가
# 두번째 반복문이 종료되면 출력, 출력 값을 연결한다.
for i in range(n):
    k = list_d[i][0]
    v = list_d[i][1]
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        elif k < list_d[j][0]:
            if v < list_d[j][1]:
                cnt += 1
    print(cnt, end=' ')