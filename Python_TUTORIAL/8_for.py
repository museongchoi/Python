# 문제 1
# 사용자로부터 input()으로 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요.
# 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
# 단, 이번에는 for 문을 사용하세요.

# num = int(input("num : "))
#
# for i in range(num):
#     print('', num)

# 문제 2
# 정수를 한 개 입력받아 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, 이번에는 for 문을 사용하세요.

# num = int(input())
#
# for i in range(1, num+1):
#     print(i, i*i)

# 문제 3
#  장치는 15초마다 온도를 측정해 프로그램에 제공한다.
# 프로그램은 먼저 최소와 최대의 안전 온도를 나타내는 두 개의 정수를 읽는다.
# 그 다음에, 장치가 제공하는 온도(정수)를 계속 읽는다. 화학 반응이 완료되면 장치는 끝을 알리는 -999를 보낸다.
# 기록된 온도가 올바른 범위에 있을 경우(최솟값 또는 최댓값과 같아도 된다) Nothing to report를 표시해야 한다.
# 하지만 온도가 위험 수준에 도달하면 Alert!를 표시하고 온도 측정을 중단한다(장치가 온도값을 계속 보내더라도).

# num = input().split()
# min = int(num[0])
# max = int(num[1])
# #min, max = map(int, input().split())
#
# tmp = int(input())
# while tmp != -999:
#     if min <= tmp <= max:
#         print("Nothing to report")
#         tmp = int(input())
#     else:
#         print("Alert")
#         break
