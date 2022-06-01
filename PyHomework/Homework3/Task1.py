# Найти НОК двух чисел
from random import randint


def find_lcm(a, b):
    x = max(a, b)
    while (True):
        if (x % a == 0) and (x % b == 0):
            lcm = x
            break
        x += 1
    return lcm


a = randint(0, 11)
b = randint(0, 11)
print(f'НОК чисел {a} и {b} равно {find_lcm(a, b)}')
