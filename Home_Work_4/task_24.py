# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

n = int(input("Кол-во кустов: "))
harvest = []

for i in range(n):
    a = int(input("Введите урожайность куста {}: ".format(i + 1)))
    harvest.append(a)

max_harvest = 0
for i in range(n):
    current_harvest = harvest[i] + (harvest[i - 1]
                                    if i > 0 else 0) + (harvest[i + 1] if i < n - 1 else 0)
    max_harvest = max(max_harvest, current_harvest)

print("Максимальное количество ягод, которое может собрать собирающий модуль: {}".format(max_harvest))