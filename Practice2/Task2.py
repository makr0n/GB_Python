# Реализуйте алгоритм перемешивания списка.


import time


def random(min, max):
    rnd = time.time()
    rnd = rnd - int(rnd)
    rnd = int(rnd * (max - min)) + min
    return rnd


spisok = ['geek', 'brains4', '5five', '3friends', '345', 'tyhgfd', '453456']
size = len(spisok)
new_spisok = []
while size > 0:
    index = random(0, size - 1)
    new_spisok.append(spisok[index])
    spisok.pop(index)
    size -= 1
print(new_spisok)
