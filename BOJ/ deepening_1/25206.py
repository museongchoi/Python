# 너의 평점은
# (학점*전평점)의 합을 학점의 총합으로 나눈것.
# P/F 인 과목 중 P인 과목은 점수에서 제외한다.
import sys
dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
subMaxsum = 0
submul = 0
ans = 0

while True:
    # 0 : 과목, 1 : 학점, 2 : 등급
    subject = list(sys.stdin.readline().split())
    if len(subject) == 0:
        break
    else:
        if subject[2] != 'P':
            subMaxsum += float(subject[1])
            submul += float(subject[1]) * dic.get(subject[2])
        elif subject[2] == 'P':
            continue

ans = submul/subMaxsum
print(ans)


