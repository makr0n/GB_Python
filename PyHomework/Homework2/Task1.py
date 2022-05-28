# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def sum_even_numbers(numbers):
    total = 0
    length = len(numbers)
    for i in range(0, length, 2):   # в цикле суммируем элементы с шагом 2
        total = total + numbers[i]
    return total


numbers_list = [1, 2, 3, 4, 5, 6, 7]
print(f'Сумма чисел списка {numbers_list} стоящих на нечетной позиции равна {sum_even_numbers(numbers_list)}')