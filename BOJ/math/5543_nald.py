# 상근 날드
bugger = 2000
drink = 2000

for _ in range(3):
    bugger = min(bugger, int(input()))
for _ in range(2):
    drink = min(drink, int(input()))

print(bugger+drink-50)