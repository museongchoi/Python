# 숫자의 합
N = int(input())
m_list = list(map(int, input().strip()))

ans = 0
for i in range(N):
    ans += m_list[i]

print(ans)