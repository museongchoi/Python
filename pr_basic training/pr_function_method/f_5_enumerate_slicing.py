#배열의 길이에 따라 다른 연산하기

def solution(arr, n):
    answer = []
    if len(arr) % 2 != 0:
        for idx, i in enumerate(arr):
            if idx % 2 == 0:
                answer.append(i + n)
            else:
                answer.append(i)
    else:
        for idx, i in enumerate(arr):
            if idx % 2 != 0:
                answer.append(i + n)
            else:
                answer.append(i)

    return answer

# def solution(arr, n):
#     N=len(arr)
#     if N%2:
#         for i in range(0,N,2): arr[i]+=n
#     else:
#         for i in range(1,N,2): arr[i]+=n
#     return arr