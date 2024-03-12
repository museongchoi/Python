# 주사위 게임 3
def solution(a, b, c, d):
    answer = 0
    arr = [a, b, c, d]
    cnt = [arr.count(i) for i in arr]

    if max(cnt) == 4:
        answer = arr[cnt.index(4)] * 1111
    elif max(cnt) == 3:
        p = arr[cnt.index(3)]
        q = arr[cnt.index(1)]
        answer = (10 * p + q) ** 2
    elif max(cnt) == 2:
        if min(cnt) == 2:
            p = arr[1]
            for i in arr:
                if p != i:
                    q = i
            answer = (p + q) * abs(p - q)
        elif min(cnt) == 1:
            tmp = []
            p = arr[cnt.index(2)]
            for i in arr:
                if p != i:
                    tmp.append(i)
            answer = tmp[0] * tmp[1]
    elif max(cnt) == 1:
        answer = min(arr)

    return answer