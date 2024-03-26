# 입력 받는 방법 1
# people = []
# for i in range(5):
#     people.append(int(input()))

# 압력 값을 int(input())로 정수로 변환하고, max 함수로 그 값과 40 중 큰 값을 반환
people = [max(40, int(input())) for i in range(5)]
#print(people)
# [40, 65, 100, 40, 95]

print(sum(people)//5)

# 방법 1
# people = [max(40, int(input())) for i in range(5)]
# sumnum = 0
# for num in people:
#     sumnum += num
# ans = sumnum//5
#
# print(ans)

# 입력값
# 10
# 65
# 100
# 30
# 95