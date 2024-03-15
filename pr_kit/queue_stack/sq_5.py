# 주식 가격
def solution(prices):
    answer = []
    l = len(prices)
    for i in range(l):
        cnt = 0
        for j in range(i + 1, l):
            if prices[i] > prices[j]:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)

    return answer