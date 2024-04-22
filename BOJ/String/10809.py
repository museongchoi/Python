# 알파벳 찾기
# 방법3. find() 이용
import string
text = input()
for x in string.ascii_lowercase:
    print(text.find(x), end = ' ')

# 방법2. for문 이용
# import string
# text = input()
# ans = string.ascii_lowercase
#
# for i in ans:
#     if i in text:
#         print(text.index(i), end=' ')
#     else:
#         print(-1, end=' ')


# 방법1(틀림)
# text = input()
# ans1 = [-1 for _ in range(26)]
# ans2 = list(map(chr, range(97, 123)))
#
# # 반복문은 text의 길이만큼 순회, i는 text의 현재 알파벳 위치 idx가 된다.
# for i in range(len(text)):
#     # idx 는 ans1이 알파벳의 위치를 모르기 때문에 ans2 알파벳 나열을 이용하여 알파벳 순번을 알려준다.
#     idx = ans2.index(text[i])
#     if ans1[idx] == -1:
#         # ans1의 알파벳 위치에 text의 알파벳 위치 i를 저장.
#         ans1[idx] = i
#
# print(ans1)