# 다이얼
# 0~9까지 다이얼, 1번을 누르는데 2초가 걸린다. 한칸 옆에 있는 숫자 1초씩 더 오래 걸린다.
al = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
text = list(input().strip())
sum = 0
for i in text:
    for j in range(len(al)):
        if i in al[j]:
            sum += j+3

print(sum)