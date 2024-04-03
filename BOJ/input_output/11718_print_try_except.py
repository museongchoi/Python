# 그대로 출력하기

while True:
    try:
        st = input()
        print(st)
    except:
        break

# input()은 EOF를 받을 때 EOFError를 일으키지만 sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴
# 따라서 sys 를 사용하려면 if 문을 사용하여 빈 문자열을 확인하고, input 사용은 try&except 를 사용.
# import sys
# while True:
#     try:
#         print(sys.stdin.readline().rstrip())
#     except EOFError:
#         break