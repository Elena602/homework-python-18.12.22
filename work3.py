# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [0.43, 1.23, 5.65, 9, 3.90, 52.32, 9.65]
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
difference = max(new_lst) - min(new_lst)
print(round(difference, 2))
lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
difference = max(new_lst) - min(new_lst)
print(round(difference, 2))