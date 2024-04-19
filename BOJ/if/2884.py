# 알람 시계
# 입력 시간 h시 m분을 의미한다. 이 시간보다 45분 앞서는 시간으로 바꾼다.
h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
else:
    m = (m + 60) - 45
    if h == 0:
        h = 23
    else:
        h -= 1
    print(h, m)