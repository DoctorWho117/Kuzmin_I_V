# -- coding: utf-8 --

""" 
    Номер зачетной книжки: 21-677.
    Автор: Кузьмин Илья Викторович, ЗИТ-21
    Дата: 27.01.2022
    Практическая работа 6
"""

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton

#Задание 2. Нахождение наименьшего делителя числа
def Z2():
	x = int(txtbx.get())
	if (x >= 2):
		i = 2
		while i <= x:
			if x % i == 0:
				Ans.configure(text = ("Наименьший делитель числа "+ str(x) + " является " + str(i)))
				break
			i += 1
	else:
		Ans.configure(text = "Число должно быть больше 2")

#Задание 6. Cреднее значение всех элементов последовательности
def Z6():
	x = float(txtbx.get())
	cnt = 0
	srzn = 0
	while x != 0:
		srzn += x
		cnt += 1
		x = float(txtbx.get())
		window.update()
	srzn /= cnt
	Ans.configure(text = ("Среднее значение элементов: " + str(srzn)))

#Задание 7. Количество элементов последовательности больших предидущего элемента
def Z7():
	x = int(txtbx.get())

	i = 0
	max = x
	while x != 0:
		if x > max:
			i += 1
		max = x
		x = int(txtbx.get())
		window.update()
	Ans.configure(text = ("Количество элементов последовательности больших предидущего элемента: "+ str(i)))

def zad():
	if selected.get() == 1:
		NameZ.configure(text="Задание 2. Нахождение наименьшего делителя числа\nВведите целое число больше 2-ки")
		Ans.configure(text = "")
		txtbx.delete(0,END)
	elif selected.get() == 2:
		NameZ.configure(text="Задание 6. Cреднее значение всех элементов последовательности\nВведите последовательность чисел, для завершения ввода введите 0")
		Ans.configure(text = "")
		txtbx.delete(0,END)
	else:
		NameZ.configure(text="Задание 7. Последовательность состоит из натуральных чисел и завершается числом 0.\nОпределите, сколько элементов этой последовательности больше предыдущего элемента.\nВведите последовательность чисел, для завершения ввода введите 0")
		Ans.configure(text = "")
		txtbx.delete(0,END)

def resh():
	if selected.get() == 1:
		Z2()
	elif selected.get() == 2:
		Z6()
	else:
		Z7()

window = Tk()
window.title("Практическая №6 Кузьмин")
window.geometry("600x300")
window.resizable(width=False, height=False)

NameZ = Label(window, text = "Выберете номер выполняемой задачи")
NameZ.grid(column = 1, row = 0)

Ans = Label(window, text = "")
Ans.grid(column = 1, row = 5)

txtbx = Entry(window, width=30)
txtbx.grid(column = 1, row = 3)
txtbx.focus()

selected = IntVar()
rad1 = Radiobutton(window,text='Первый', value=1, variable=selected, command = zad)
rad2 = Radiobutton(window,text='Второй', value=2, variable=selected, command = zad)
rad3 = Radiobutton(window,text='Третий', value=3, variable=selected, command = zad)
rad1.grid(column = 0, row = 2)
rad2.grid(column = 0, row = 3)
rad3.grid(column = 0, row = 4)

butn = Button(window, text = "Выполнить", command = resh)
butn.grid(column = 1, row = 4)
window.mainloop()