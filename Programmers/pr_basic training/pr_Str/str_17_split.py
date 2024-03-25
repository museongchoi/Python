# x 사이의 개수
def solution(myString):
    answer = []
    my_list = myString.split('x')
    for i in my_list:
        answer.append(len(i))
    return answer

def solution(myString):
    return [len(w) for w in myString.split('x')]