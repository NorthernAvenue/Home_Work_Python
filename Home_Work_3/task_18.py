# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X | 5
# 1 2 3 4 5 массив
# 6 элемент для которого ищем ближайшее по значению число
# -> 5 результат

import random

size = int(input("Размер: "))
array = []

for i in range(size):
    index = random.randint(1, 20)
    array.append(index)

print(array)

x = int(input("Число для которого ищем самое близкое значение: "))

# список для хранения всех значений по условию, если их больше 1
closest_number = [array[0]]
min_diff = closest_number[0] - x

if closest_number[0] < x:
    min_diff = x - closest_number[0]

for ellement in array[1:]:
    diff = ellement - x
    if ellement < x:
        diff = x - ellement
    if diff < min_diff:
        closest_number = [ellement]
        min_diff = diff
    elif diff == min_diff:
        closest_number.append(ellement)

print(closest_number)
