# 단어 공부
# 입력된 단어에 가장 많이 사용된 알파벳을 출력
import string
text = input()
text = text.upper()
e = list(string.ascii_uppercase)
vi = [0 for _ in range(26)]

for k in text:
    if k in e:
        vi[e.index(k)] += 1

cnt = max(vi)
if vi.count(cnt) >= 2:
    print('?')
else:
    print(e[vi.index(cnt)])