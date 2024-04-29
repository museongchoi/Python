# 배수와 약수
# 입력으로 들어오는 두 수가 같을 수 없고, 마지막 입력은 0이 2개 들어온다.

while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break

    if x < y and y%x == 0:
        print('factor')
    elif x > y and x%y == 0:
        print('multiple')
    else:
        print('neither')
