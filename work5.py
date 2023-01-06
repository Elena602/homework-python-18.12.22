# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def findFib(index):
    if index == 0:
        return 0
    if index > 0:
        if index == 1: return 1
        return findFib(index - 1) + findFib(index - 2)
    if index < 0:
        return findFib(index + 2) - findFib(index + 1)
n = int(input("Введите количество чисел:\n"))
lst = [findFib(i) for i in range(-n, n + 1)]
print(lst)