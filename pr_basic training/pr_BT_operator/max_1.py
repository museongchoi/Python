# 두 수의 연산값 비교하기
def solution(a, b):
    answer = 0
    num1 = str(a) + str(b)
    num2 = 2 * a * b
    answer = max(int(num1), num2)
    return answer