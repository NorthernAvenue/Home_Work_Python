# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input("Первый элемент прогрессии: "))
d = int(input("Шаг между соседними элементами: "))
n = int(input("Кол-во элементов : "))

progression = [a1 + (i-1)*d for i in range(1, n+1)]

print(*progression)




