n = int(input())
num = input()

arr = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]
# 'a'부터 'i'까지의 ASCII 코드 범위를 생성하고, 각 코드에 해당하는 문자로 변환
chars = [chr(i) for i in range(ord('a'), ord('j'))]
dic = dict(zip(arr, chars))
key = list(dic.keys())

text = []
chunk_size = 6
for i in range(0, len(num), chunk_size):
    text.append(num[i:i+chunk_size])
answer = "" # 출력 문자열
value = ""  # 딕셔너리에 해당 문자가 있는지 없는지, 있다면 해당 문자열 반환 없다면 None 반환
cnt = 0     # 해당 문자가 없을시 처음 나오는 문자의 위치
indx = -1
for el in text:
    value = dic.get(el) # 문자열에 해당하는 딕셔너리 키 찾기, 없으면 None
    cnt += 1
    if value is None:   # None 값이 반환 됬을 때 키값에서 문자가 하나만 틀렸으면 같다고 판단
        #flag = False        # key 를 다 돌았는지 확인하는 kcnt
        for k in key:   # key 배열을 돌면서 현재 el 값과 확인, 하나 이상의 문자가 틀렸는지 즉, 하나만 틀렸을 경우 같은 문자열이라 판단
            cnt1 = 0    # 틀린 문자 개수 2 이상인지 찾는 cnt1
            for j in range(6):  # 현재 key의 문자를 하나씩 확인
                if el[j] != k[j]:
                    cnt1 += 1
            if cnt1 == 1:   # 문자가 하나만 틀렸을 경우 같은 문자라 판단, 해당 문자 key의 값을 문자열에 더한 후 반복문 빠져나옴
                answer += dic.get(k)
                #flag = True #하나라도 걸림(숫자 하나 다른것과)
                break
        else:
            indx = cnt
            break
        # if not flag:   # if flag == False
        #     indx = cnt
        #     break
    else:
        answer += value
if indx != -1:
    print(cnt)
else:
    print(answer.upper())



# n = int(input())
# num = input()
#
# arr = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]
# # 'a'부터 'i'까지의 ASCII 코드 범위를 생성하고, 각 코드에 해당하는 문자로 변환
# chars = [chr(i) for i in range(ord('a'), ord('j'))]
# dic = dict(zip(arr, chars))
# key = list(dic.keys())
#
# text = []
# chunk_size = 6
# for i in range(0, len(num), chunk_size):
#     text.append(num[i:i+chunk_size])
#
# answer = "" # 출력 문자열
# indx = -1   # 해당 문자가 없을시 처음 나오는 문자의 위치
# value = ""  # 딕셔너리에 해당 문자가 있는지 없는지, 있다면 해당 문자열 반환 없다면 None 반환
# cnt = 0
# for el in text:
#     value = dic.get(el)
#     cnt += 1
#     if value is None:
#         for i in key:
#             cnt1 = 0
#             for j in range(6):
#                 if el[j] != i[j]:
#                     cnt1 += 1
#             if cnt1 == 1:
#                 answer += i
#                 break
#         if cnt1 != 1:
#             indx = cnt
#             break
#     else:
#         answer += value
# if indx != -1:
#     print(indx)
# else:
#     print(answer.upper())

#011111000000011111000000111011 : BABAF 인데 출력값은 5
#011111000000011111000000110100 : BABAG 인데 출력값도 BABAG