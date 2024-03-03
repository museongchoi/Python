# 문제 1
#input()을 사용해 사용자로부터 입력받은 숫자를 한글로 출력하는 프로그램을 작성하세요. 단, 사용자는 1 이상 3 이하의 정수 중 하나를 입력한다고 가정합니다.

# num = int(input("1~3 num : "))
#
# if num == 1:
#     print('일')
# elif num == 2:
#     print('이')
# elif num == 3:
#     print('삼')
# else:
#     print("1 ~ 3 정수 중 하나를 입력하세요")

# 문제 2
#input()으로 사용자의 나이를 입력받은 후, 다음 표의 어느 세대에 속하는지 출력하세요. 입출력 문구는 자유롭게 지으면 됩니다.
#~1924	가장 위대한 세대(The Greatest Generation)
#1925~1945	침묵 세대(The Silent Generation)
#1946~1964	베이비붐 세대(baby boomer)
#1965~1980	X세대(Generation X)
#1981~1996	밀레니얼(millennial)
#1997~	Z세대(Generation Z)

# num = int(input("나이 : "))
# if num <= 1924:
#     print("가장 위대한 세대")
# elif num >= 1925 and num <= 1945:
#     print("침묵 세대")
# elif num >= 1946 and num <= 1964:
#     print("베이비붐 세대")
# elif num >= 1965 and num <= 1980:
#     print("X 세대")
# elif num >= 1981 and num <= 1996:
#     print("밀레니얼 세대")
# else:
#     print("Z세대")

#추가 문제
#베이비붐 세대 확인 코드를 설명드리면,
#① 1963년생까지는 미국인과 한국인 모두 베이비붐 세대이므로 국적을 묻지 않아도 되고,
#② 1964년생이면서 ③ 미국인일 경우(한국인이 아닐 경우) ④ 베이비붐 세대입니다.

# elif y <= 1963 or (  # ①
#         y <= 1964 and  # ②
#         input("Are you Korean?(y/n) ").lower()[0] != 'y'  # ③
#     ):
#     gen = 'a baby boomer'  # ④


# 문제 3
#백만 이상의 숫자를 입력받았을 때 1~10만자리 숫자를 생략하고 ‘M’을 붙여서 출력하게 코드를 수정해 보세요.

# num = int(input("num :"))
# result = str(num)
#
# if num >= 1000000:
#     result = str(num // 1000000) + 'M'
#
# print(result)

# 문제 4
# input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가, 음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는 파이썬 스크립트를 작성하세요.

# sum = 0
#
# while True:
#     num = int(input("num : "))
#     if num < 0:
#         print(sum)
#         break
#     sum += num

