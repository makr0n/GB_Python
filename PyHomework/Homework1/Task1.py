"""
Сформировать список из N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.
"""


def geometric_progression(start, multiplier, sequencelength):

    sequence = [start*multiplier**(i-1) for i in range(1, sequencelength + 1)]
    return sequence


print(geometric_progression(1, -3, 5))
