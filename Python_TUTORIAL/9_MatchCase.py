# 1 ~ 10 정수 중 홀수, 짝수 판별
for n in range(1, 11):
	if n % 2 == 0:
		print(f"{n} is even.")
	elif n % 2 == 1:
		print(f"{n} is odd.")