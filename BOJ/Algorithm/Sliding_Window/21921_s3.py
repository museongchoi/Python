# 블로그
# 블로그 시작한 날짜 총 n일, x일 동안 가장 많이 들어온 인원수와 최대 인원 수 기간 개수를 출력
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visited_ch = list(map(int, input().split()))
window = sum(visited_ch[:x])
tmp = [] # 가장 많이 들어온 인원 수와 기간 개수를 구하기 위한 리스트
tmp.append(window)
ans = window # 최대 윈원 수


for k in range(x, n):
    window += visited_ch[k] - visited_ch[k-x]
    tmp.append(window)
    ans = max(ans, window)

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(tmp.count(ans))




