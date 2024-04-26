# 그룹 단어 체커
# 연속적으로 있는 단어는 그룹이고, 앞에 나온 단어가 비연속적으로 뒤에 나온다면 비그룹이다.
n = int(input())
cnt = n
for _ in range(n):
    text = input()
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            pass
        elif text[i] in text[i+1:]:
            cnt -= 1
            break

print(cnt)