# 문자열
# n : 문자열 입력 개수
# 문자열의 첫번째 문자와 마지막 문자를 출력하라
n = int(input())

for _ in range(n):
    text = input()
    print(text[0]+text[-1])