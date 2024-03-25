# 접두사인지 확인하기

def solution(my_string, is_prefix):
    answer = int(my_string.startswith(is_prefix))

    return answer

# def solution(my_string, is_prefix):
#     my_list = []
#     for i in range(1, len(my_string)):
#         my_list.append(my_string[:i])
#     answer = int(is_prefix in my_list)
#     return answer
