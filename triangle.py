# Яндекс. Тренировки по алгоритмам июнь 2021, занятие 1
# B. Треугольник

def main():
	a = int(input())
	b = int(input())
	c = int(input())
	if a + b > c and b + c > a and a + c > b:
		print('YES')
	else:
		print('NO')
main()
