# 1
# 1로만 이루어져 있는 n의 배수중 가장 작은 자리수를 구한다.

while True:
    # 입력 값이 들어오지 않는다면 종료.
    try:
        n = int(input())
    except:
        break

    t_num = 1   # 1 -> 11 -> 111
    cnt = 1     # 자리수 cnt
    while True:
        # 0으로 나누어지면 1로 이루어진 n의 배수 중 가장 작은 자리수
        if t_num % n == 0:
            break
        else:
            # 1로 이루어진 숫자 증가.
            t_num = t_num * 10 + 1
            cnt += 1
    print(cnt)