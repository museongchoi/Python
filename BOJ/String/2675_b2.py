# 문자열 반복
# n : 문자열 입력 횟수
# x : 문자 반복 횟수, text : 문자열
n = int(input())
for _ in range(n):
    x, text = map(str, input().split())
    for i in text:
        print(i*int(x), end='')
    print()