# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random

size = int(input("Размер списка : "))
list_1 = [random.randint(-10, 20) for _ in range(size)]
print(f"Исходный список : ", list_1)

result = []
print("Введите диапазон")
x = int(input("От: "))
y = int(input("До: "))

for i, value in enumerate(list_1):
    if x <= value <= y:
        result.append(i)

print(f"Релультат : ", result)