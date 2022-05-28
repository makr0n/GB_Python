# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def multiplying_pairs_of_numbers(numbers):
    length = len(numbers)
    pairs = []
    multiply = 0
    if length % 2 == 0:                                                 #Производим проверку на четность длины списка, для дальнейшего нахождения индекса середины списка
        for i in range(length // 2):                                    #Если условие четности выполняется, делим без остатка длину списка на 2
            multiply = numbers[i] * numbers[length - i - 1]             #Получаем произведение пар чисел
            pairs.append(multiply)
    else:
        for i in range(length // 2 + 1):                                #Иначе делим без остатка длину списка на 2 и прибавляем 1
            multiply = numbers[i] * numbers[length - i - 1]
            pairs.append(multiply)
    return pairs


odd_list = [2, 3, 5, 6, 4]
even_list = [2, 3, 5, 6]

print(f'Произведение пар чисел в списке {odd_list} равно {multiplying_pairs_of_numbers(odd_list)}')
print(f'Произведение пар чисел в списке {even_list} равно {multiplying_pairs_of_numbers(even_list)}')
