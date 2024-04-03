# idx 7 이되면 0으로 초기화
x, y = map(int, input().split())
alist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = 0

# 7일 기준 돌아오는 요일은 같다. 달마다 바뀌는 1일이 몇요일인지 계산을 하면 된다.
# 입력된 x 월 전까지에 각 월의 일수를 더한다.
# y를 더한 뒤 7일 기준이므로 나눈다.
# 나머지가 week의 idx 값이다.
for i in range(x-1):
    day += alist[i]

day = (day+y) % 7
print(week[day])
