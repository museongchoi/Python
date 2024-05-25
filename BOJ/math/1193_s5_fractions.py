# 분수 찾기
n = int(input())
line = 1

# n이 해당하는 대각선(line)을 구하는 반복문.
# 1번째 line 요소개수 1개, 2번째 2개, 3번째 3개
# 그러므로 n이 해당하는 line을 구하기 위해 line(요소개수)을 빼주고, 동시에 line + 1 증가
while n > line:
    n -= line
    line += 1

# 대각선(line)이 짝수일때 분자는 오름차순, 분모는 내림차순 / 홀수는 반대.
# 분자(a)는 그대로 n, 분모(b)는 line - n + 1
if line%2 == 0:
    a = n   # 분모는 그대로 n은 몇번째인지 구한 값이기 때문이다.
    b = line - n + 1    # 해당 line 의 n 번째에 있으므로 line-n을 해주고 인덱싱에 의한 + 1
elif line%2 == 1:
    a = line - n + 1
    b = n

print(f'{a}/{b}')