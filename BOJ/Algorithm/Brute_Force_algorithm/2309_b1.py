# 일곱 난쟁이
# 아홉 줄에 걸쳐 난쟁이들의 키가 주어진다.
import sys
input = sys.stdin.readline
li = [int(input()) for i in range(9)]

li.sort()
ans = sum(li)
fake = []
for i in range(9):
    for j in range(i+1, 9):
        if len(fake) == 2:
            continue
        if ans - li[i] - li[j] == 100:
            fake.append(li[i])
            fake.append(li[j])


for i in li:
    if i in fake:
        continue
    else:
        print(i)



# 방법 2
# array = []
# for i in range(9):
#     array.append(int(input()))
#
# array.sort()
#
# sum_ = sum(array)
#
# # 만약 모두다 더하고 2명을 뺐을 때 그 값이 100이라면 2개를 뺀 나머지 값들 출력
# for i in range(len(array)):
#     for j in range(i + 1, len(array)):
#         if sum_ - array[i] - array[j] == 100:
#             for k in range(len(array)):
#                 if k == i or k == j:
#                     pass
#                 else:
#                     print(array[k])
#             exit()