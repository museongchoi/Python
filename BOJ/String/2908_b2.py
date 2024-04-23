# 상수
# 입력된 두 숫자를 거꾸로 읽고, 그 중 큰 숫자를 출력
# 1. 두개의 문자열로 리스트를 생성.
# 2. 각 문자열을 슬라이싱으로 뒤집기.
# 3. 큰 숫자를 출력
# 방법2
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
print(max(a,b))

# 방법1
# num = input().split()
# a = num[0][::-1]
# b = num[1][::-1]
# print(max(a,b))
