# 배열에 따른 문자열 대소문자 변환하기
def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())

    return answer