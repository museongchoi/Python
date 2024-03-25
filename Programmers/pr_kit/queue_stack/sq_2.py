# 올바른 괄호
def solution(s):
    answer = True
    l = []

    for i in s:
        if i == '(':
            l.append(i)
        elif len(l) == 0 or l.pop() != '(':
            return False
    if len(l) != 0:
        return False

    return True