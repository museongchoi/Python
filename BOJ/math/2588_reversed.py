#곱셈
# a,b 의 곱셈 과정의 값들을 출력

a = int(input())
b = int(input())
strb = str(b)
# print(len(str(b))), int 타입 b 의 길이를 구하려면 str로 형 변환 해야함.

for i in reversed(range(len(strb))):
    print(a*int(strb[i]))

print(a*b)

# a = int(input())
# b = int(input())
# ans = []
# ans.append(a * (b%10))
# ans.append(a * ((b//10) % 10))
# ans.append(a * (b//100))
# ans.append(a * b)
#
# for i in ans:
#     print(i)