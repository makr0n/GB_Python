# Реализовать алгоритм задания случайного числа без генератора случайных чисел


import time


def random(min, max):
    rnd = time.time()
    rnd = rnd - int(rnd)
    rnd = int(rnd * (max - min)) + min
    return rnd


print(random(50, 79))
