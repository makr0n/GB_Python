# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math


def fractional_part(number):
    new_list = []
    for i in range(len(number)):
        if (number[i] - math.trunc(number[i])) != 0:  # Добавляем проверку на наличие целых чисел
            new_list.append(number[i] - math.trunc(number[i]))
    return new_list


fractional_numbers = [1.1, 1.2, 3.1, 5, 10.01, 6, 1.15]
frac = fractional_part(fractional_numbers)
print(f'Полученные дробные части {frac}')

diff = round((max(frac) - min(frac)), 2)  # Добавил округление числа, чтобы получить вид ответа как в примере
print(f'Разница между максимальным и минимальным значением дробной части элементов равна {diff}')
