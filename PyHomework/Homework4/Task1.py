# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

from random import randint

n = randint(5, 15)
with open('random_numbers.txt', 'w') as data:
    for i in range(1, n + 1):
        number = randint(0, 101)
        data.writelines(str(number) + '\n')


def sort_list(nonsorted_list):
    for item in range(len(nonsorted_list)):
        for j in range(0, (len(nonsorted_list) - item - 1)):
            if nonsorted_list[j] > nonsorted_list[j + 1]:
                (nonsorted_list[j], nonsorted_list[j + 1]) = (nonsorted_list[j + 1], nonsorted_list[j])
    return nonsorted_list


def get_sorted_file(file_name):
    data = open(file_name, 'r')
    nonsorted_list = data.readlines()
    for i in range(len(nonsorted_list)):
        nonsorted_list[i] = int(nonsorted_list[i])
    data.close()
    print(nonsorted_list)
    sorted_list = sort_list(nonsorted_list)
    data = open(file_name, 'w')
    for i in range(len(sorted_list)):
        data.writelines(str(sorted_list[i]) + "\n")
    print(sorted_list)
    data.close()


get_sorted_file('random_numbers.txt')
