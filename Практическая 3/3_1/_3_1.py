# -- coding: utf-8 --

"""
	Номер зачетной книжки 21-676
	Автор: Кузьмин Илья Викторович
	Дата: 26.01.2022
	Практическая 3. Задание 2. Даны два целых числа A и В. Выведите все числа от A до B включительно, 
							   в порядке возрастания, если A < B, или в порядке убывания в противном случае.
"""

print('Введите 2 числа')
print('Введите число A')
A = int(input()) 
print('Введите число B')
B = int(input()) 

if A < B:
	for i in range(A,B+1):
		print (i)
else:
	for i in range(A,B-1,-1):
		print (i)