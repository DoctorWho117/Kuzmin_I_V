# -- coding: utf-8 --

"""
	Номер зачетной книжки 21-676
	Автор: Кузьмин Илья Викторович
	Дата: 26.01.2022
	Практическая 5. Задание 2. Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
"""

print("Введите целое число больше 2-ки")
x = int(input())

if (x >= 2):
	i = 2
	while i <= x:
		if x % i == 0:
			print("Наименьший делитель числа ",x," является ",i)
			break
		i += 1
else:
	print("Число должно быть больше 2")