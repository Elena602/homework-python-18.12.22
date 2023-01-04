# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [27, 13, 5, 95, 3, 52, 9]
def sum_of_odd_index(list):
    s = 0
    for i in range(len(list)):
        if i % 2 != 0:
            s += list[i]
    print(f"Сумма равна: {s}")
sum_of_odd_index(list)