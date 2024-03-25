# 코드 처리하기
def solution(code):
    answer = ''
    ret = []
    mode = 0
    for idx, i in enumerate(code):
        if i == '1':
            if mode == 1:
                mode = 0
            else:
                mode = 1
        elif i != '1':
            if idx%2 == 0 and mode == 0: # 짝수 1아님 mode 0
                ret.append(i)
            elif idx%2 == 1 and mode == 1: # 홀수 1아님 mode 1
                ret.append(i)
    if not ret:
        answer = 'EMPTY'
    else:
        answer = ''.join(str(e) for e in ret)
    return answer