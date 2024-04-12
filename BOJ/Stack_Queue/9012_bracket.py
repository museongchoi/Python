# 괄호
import sys
n = int(input())

for _ in range(n):
    bracket = list(map(str, sys.stdin.readline().strip()))
    bol = False
    st = []

    for i in bracket:
        if i == '(':
            st.append(i)
        elif i == ')':
            if len(st) == 0:
                bol = True
                break
            else:
                st.pop()

    if len(st) != 0 or bol == True:
        print('NO')
    else:
        print('YES')
