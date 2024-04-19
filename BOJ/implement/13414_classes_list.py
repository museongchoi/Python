# 수강신청
# 수강학번을 문자열로 받아야 오류가 나지 않음.
# 수강 가능 인원 k, 수강 신청 횟수 l, l번 학번이 입력으로 들어온다.
import sys
k, l = map(int, sys.stdin.readline().split())

# 수강 신청이 들어온 순서대로 학번과 순서를 딕셔너리에 key, value로 저장.
ans = {}
for i in range(l):
    tmp = sys.stdin.readline().rstrip()
    ans[tmp] = i

# 람다식을 이용하여 sorted함수의 매개변수인 key(기준) = x[1] 즉, value를 기준으로 정렬을 하는 것이다.
# x[0]은 딕셔너리의 key를 기준으로 정렬.
result = sorted(ans.items(), key = lambda x:x[1])

# 수강 가능 인원보다 신청 인원이 작다면 수강 가능 인원 k를 신청 인원과 같게 만든다.
if len(result) < k:
    k = len(result)

for j in range(k):
    print(result[j][0])
