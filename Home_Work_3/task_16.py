# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# массив 5 1 2 3 4 5
# искомое 3
# -> ответ 1

import random

size = int(input("Размер массива : "))
array = []

for i in range(size):
    index = random.randint(1, 10)
    array[i:i] = [index]

print(array)

x = int(input("Введите искомое число: "))
count = 0

for i in range(size):
    if array[i] == x:
        count += 1

print(count)
