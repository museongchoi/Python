# # for 문이 다 진행된 후 else 실행
# for x in [1,2,3,4]:
# 	print(x)
# else:
# 	print("리스트의 원소를 모두 출력했어요")
#
# # else 앞에 for문 안에 break가 등장 시 else 문이 동작하지 않음
# for x in [1,2,3,4]:
# 	if x%3 != 0: # 3의 배수가 아니면 출력
# 		print(x)
# 	else:
# 		break
# else:
# 	print("리스트의 원소를 모두 출력했어요")
#
# # while - else 동일
# countdown = 5
# while countdown > 0:
# 	print(countdown)
# 	countdown -= 1
# 	if input() == '중단':
# 		break
# else:
# 	print("발사")