# 약수들의 합
# 입력이 -1 이면 종료
# 약수 구하기, 입력값을 순회(1~입력값까지)를 돌면서 나누어 떨어질때 값들을 리스트에 저장.
# 해당 리스트에 값들을 더하여 입력값과 같다면 완전수, 아니라면 '입력값 is NOT perfect' 출력.

while True:
    num = int(input())
    divisor = []
    if num == -1:
        break
    for i in range(1, num):
        if num%i == 0:
            divisor.append(i)
    #print(divisor)
    if num == sum(divisor):
        divisor.sort()
        print(num, '=', ' + '.join(map(str, divisor)))
    else:
        print(f'{num} is NOT perfect.')