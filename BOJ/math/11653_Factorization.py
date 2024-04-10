# 소인수분해

# 방법 2
n = int(input())
i = 2
while n > 1:
    if n%i == 0:
        print(i)
        n = n//i
    else:
        i += 1


# 방법 1
# n = int(input())
#
# if n == 1:
#     print('')
# else:
#     for i in range(2, n+1):
#         if n%i == 0:
#             while n%i == 0:
#                 print(i)
#                 n = n // i
