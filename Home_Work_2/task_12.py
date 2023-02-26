# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import math

while True:
    s = input("Сумма = ")
    p = input("Произведение = ")

    if not s.isdigit() or not p.isdigit():
        print("Сумма и произведение должны быть натуральными числами")
        continue

    s = int(s)
    p = int(p)

    if s < 1 or p < 1:
        print("Сумма и произведение должны быть натуральными числами")
        continue

    discriminant = s**2 - 4 * p

    if discriminant < 0:
        x = y = s / 2
        print(f"Оба числа равны{int(x)}")
    else:
        x = round((s - math.sqrt(discriminant)) / 2)
        y = round((s + math.sqrt(discriminant)) / 2)
        if x < 1 or x > 1000 or y < 1 or y > 1000:
            print("x и y должны быть натуральными числами, не превышающими 1000")
        else:
            if x + y == s and x * y == p:
                print(f"Первое число = {int(x)}, второе = {int(y)}")
                break
            else:
                print("Некорректное решение")


# Решение без библиотеки и обработки исключей и условий
# s = int(input("Сумма = "))
# p = int(input("Произведение = "))
# D = s*s - 4*p

# if D < 0:
#     print("Решений нет")
# elif D == 0:
#     x = s // 2
#     y = s // 2
#     if x * y == p:
#         print(x, y)
#     else:
#         print("Решений нет")
# else:
#     x1 = (s - int(D**0.5)) // 2
#     x2 = (s + int(D**0.5)) // 2
#     if x1 * x2 == p:
#         print(x1, x2)
#     else:
#         print("Решений нет")
