# # num = 1
# # while num <= 100:
# #     print(num)
# #     num += 1
#
# # 문제 1
# #input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
# #단, while 문을 사용하세요.
#
# # num = int(input("반복 값&횟수 : "))
# # cnt = 1
# # while cnt <= num:
# #     print(num)
# #     cnt += 1
#
# def solution(arr, queries):
#     answer = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
#     arr = [list(map(int, input().split())) for _ in range(10)]
#
#     arr2 = list(input().split())
#     # input : 1 2 3 4
#     # arr2 = ["1", "2", "3", "4"]
#
#     arr3 = list(map(int, input().split()))
#     # input : 1 2 3 4
#     # arr3 = [1, 2, 3, 4]
#
#     arr4 = [list(input().split())]
#     # input : 1 2 3 4
#     # arr4 = [["1", "2", "3", "4"]]
#
#     arr5 = [i for i in range(10)]
#     # arr5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#     arr6 = [list(input().split()) for _ in range(10)]
#     # input
#     # 1 2 3
#     # 4 5 6
#     # 7 8 9
#     # 2 3 4
#     # 5 6 7
#     # 8 9 10
#     # 3 4 5
#     # 6 7 8
#     # 9 10 11
#     # 1 2 3 4
#     # arr6 =
#     # ['1', '2', '3']
#     # ['4', '5', '6']
#     # ['7', '8', '9']
#     # ['2', '3', '4']
#     # ['5', '6', '7']
#     # ['8', '9', '0']
#     # ['3', '4', '5']
#     # ['6', '7', '8']
#     # ['9', '0', '1']
#     # ['1', '5', '9']
#
#     arr7 = [list(map(int, input().split())) for _ in range(10)]
#     # input :
#     # 1 2 3
#     # 4 5 6
#     # 7 8 9
#     # 2 3 4
#     # 5 6 7
#     # 8 9 0
#     # 3 4 5
#     # 6 7 8
#     # 9 0 1
#     # 1 5 9 5
#     #arr 7:
#     # [1, 2, 3]
#     # [4, 5, 6]
#     # [7, 8, 9]
#     # [2, 3, 4]
#     # [5, 6, 7]
#     # [8, 9, 0]
#     # [3, 4, 5]
#     # [6, 7, 8]
#     # [9, 0, 1]
#     # [1, 5, 9, 5]
#
#     return answer
# arr6 = [list(map(int, input().split())) for _ in range(10)]
# #arr6 = [list(input().split()) for _ in range(10)]
# for i in arr6:
#     print(i)


arr = [1, 2, 3, 4, 5]
arr[2]

#-------------------
def solution(arr, queries):
    answer = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

    # arr = [list(map(int, input().split())) for _ in range(10)]
    group = [{"이름": '김재헌', "나이": 45}, {"이름": '최무성', "나이": 35}, {"이름": '고기찬', "나이": 25}]
    for person in group:
        print(person["이름"])
        print(person["나이"])
    이차원배열 = [
        [2, 3],
        [2, 2],
        [4, 6]
    ]
    for 줄 in 이차원배열:
        for 줄내의원소 in 줄:
            print(줄내의원소, end=" ")
        print()

    # arr2 = list(input().split())
    # input : 1 2 3 4
    # arr2 = ["1", "2", "3", "4"]

    # arr3 = list(map(int, input().split()))
    # input : 1 2 3 4
    # arr3 = [1, 2, 3, 4]

    # arr4 = [list(input().split())]
    # input : 1 2 3 4
    # arr4 = [["1", "2", "3", "4"]]

    # arr5 = [i for i in range(10)]

    # a = int(["1", "2", "3"])
    # print(a)
    # for s,e in queries:
    #    for
    # for s, e in queries:

    return answer