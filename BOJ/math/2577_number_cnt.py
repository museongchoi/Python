# 숫자의 개수
# 0 ~ 9 까지 각 숫자가 계산된 결과에 몇번 쓰였는지.

muti = 1
for i in range(3):
    n = int(input())
    muti *= n
tmp = str(muti)

for num in range(10):
    cnt = 0
    for n in range(len(tmp)):
        if str(num) == tmp[n]:
            cnt += 1
    print(cnt)
