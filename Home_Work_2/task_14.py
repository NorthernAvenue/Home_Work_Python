# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число: "))

for i in range(n):
    if pow(2,i) > n:
        break
    else:
        print(pow(2,i))
    
# без pow 
# n = int(input("Введите число: "))
# result = 1

# for i in range(n):
#     print(result)
#     result *=2
#     if result > n:
#         break

