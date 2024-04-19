# 세로 읽기
# A~Z / a~z / 0~9 까지 입력이 5x5 들어온다.
# 이를 세로로 읽은 글자들을 출력해라.
import sys
st = ['' for _ in range(15)]

# 세로로 읽을때 몇번째에 있는 글자인지 알아야 한다.
# 입력을 받은 뒤에 글자의 idx를 사용하여 몇번째 글자인지 알고, st의 idx번째에 저장한다.
for i in range(5):
    tmp = sys.stdin.readline().strip()
    for j in range(len(tmp)):
        st[j] += tmp[j]

# st 리스트 안에 ' '이 나오면 멈춤. 저장되있는 문자열만 출력하기 위해.
ans = ''
for k in st:
    if k == '':
        break
    ans += k
print(ans)