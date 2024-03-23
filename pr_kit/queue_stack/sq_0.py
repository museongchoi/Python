# 같은 숫자는 싫어
def solution(arr):
    answer = []

    for i in arr:
        # answer 길이 0, 값이 존재 하지 않음.
        if len(answer) == 0:
            answer.append(i)
        # stack 맨 위값, 리스트의 맨 끝 값 과 i값을 비교, 같으면 넘어간다.
        elif answer[-1] == i:
            continue
        # 값이 같지 않으면 추가
        else:
            answer.append(i)
    return answer


def solution(arr):
    answer = []
    #print(range(1, len(arr)))
    answer.append(arr[0])
    # arr의 idx 0 의 값을 추가
    # 1 부터 arr 길이까지
    # 현재 idx 값이 idx-1 의 값과 같으면 연속적, 다르면 연속적이지 않으므로 추가
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer