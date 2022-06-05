# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
import math


def get_pi(d):
    reference_pi = 4 * math.atan(1)
    pi = 0
    k = 0
    while (abs(reference_pi - pi) > d):
        pi += (1 / (16 ** k)) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))  # Формула Бэйли-Боруэйна-Плаффа
        k += 1

    print(f'Референсное значение числа Пи: {reference_pi}')
    print(f'Вычисленное значение числа Пи: {pi}')


get_pi(0.00048)
