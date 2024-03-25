# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer


# def solution(arr):
#     return [i for i in arr for j in range(i)]