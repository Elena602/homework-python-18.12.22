# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
List = [2, 3, 4, 5, 6]

def multiplication(List):
    length = len(List)//2 + 1 if len(List) % 2 != 0 else len(List)//2
    new_list = [List[i]*List[len(List)-i-1] for i in range(length)]
    print(new_list)

multiplication(List)
List = list(map(int, input("Введите числа через пробел:\n").split()))
multiplication(List)