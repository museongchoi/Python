# 수열과 구관 쿼리2
# 인덱스 범위 안에 값을 비교하면 된다

def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        el = []
        for i in arr[s:e + 1]:
            if i > k:
                el.append(i)

        answer.append(-1 if not el else min(el))

    return answer


# def solution(arr, queries):
#     answer = []
#
#     for s, e, k in queries:
#         el = []
#         for i in arr[s:e + 1]:
#             if i > k:
#                 el.append(i)
#
#         if len(el) == 0:
#             answer.append(-1)
#         else:
#             answer.append(min(el))
#
#     return answer