A, B = map(int, input().split())
d = ['+', '-', '*', '//', '%']

for i in d:
    if i == '+':
        print(A + B)
    elif i == '-':
        print(A - B)
    elif i == '*':
        print(A * B)
    elif i == '//':
        print(A // B)
    elif i == '%':
        print(A % B)


# A, B = map(int, input().split())
# d = ['+', '-', '*', '//', '%']
# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)
