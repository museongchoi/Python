# 그룹 단어 체커
# 연속적으로 있는 단어는 그룹이고, 앞에 나온 단어가 비연속적으로 뒤에 나온다면 비그룹이다.
n = int(input())
# 연속적인 단어를 뽑는 것이므로, 연속적인 단어의 총 개수는 n개이다. 비연속적인 단어일시 개수를 뺀다.
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