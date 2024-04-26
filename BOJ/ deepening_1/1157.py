# 단어 공부
# 입력된 단어에 가장 많이 사용된 알파벳을 출력
# 방법2
word = input().upper()
# 입력 받은 word 단어의 중복값을 지운 리스트
word_list = list(set(word))

# 사용된 알파벳이 몇번 사용되었는지 확인하는 반복문
# count 함수를 사용하여 word 단어에 순회하는 i의 알파벳이 얼마나 사용되었는지 cnt 리스트에 저장한다.
cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])

# 방법1
# import string
# text = input()
# text = text.upper()
# e = list(string.ascii_uppercase)
# vi = [0 for _ in range(26)]
#
# for k in text:
#     if k in e:
#         vi[e.index(k)] += 1
#
# cnt = max(vi)
# if vi.count(cnt) >= 2:
#     print('?')
# else:
#     print(e[vi.index(cnt)])