# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dvoichnoe_chislo = ""
n = int(input("Введите число для преобразования:\n"))
while n != 0:
    dvoichnoe_chislo = str(n % 2) + dvoichnoe_chislo
    n //= 2
print(dvoichnoe_chislo)