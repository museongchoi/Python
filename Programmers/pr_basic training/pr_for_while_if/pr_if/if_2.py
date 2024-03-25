# 홀짝에 따라 다른 값 반환하기
def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % 2 == 1 and i % 2 == 1:
            answer += i
        elif n % 2 == 0 and i % 2 == 0:
            answer += i * i

    return answer