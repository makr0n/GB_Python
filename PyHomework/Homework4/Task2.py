# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]


def get_longest_sequence(numbers):
    n = len(numbers)
    lis = [1] * n
    parent = [-1] * n

    for i in range(n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    parent[i] = j
    length = 0
    pos = 0
    for i in range(n):
        if length < lis[i]:
            length = lis[i]
            pos = i

    sequence = []
    while pos != -1:
        sequence.append(numbers[pos])
        pos = parent[pos]
    sequence.reverse()
    print(sequence)

first_list = [1, 5, 2, 3, 4, 6, 1, 7]
second_list = [5, 2, 3, 4, 6, 1, 7]

get_longest_sequence(first_list)
get_longest_sequence(second_list)
