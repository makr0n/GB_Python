# 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1.
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.

# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

from functools import reduce

prog_lang = ['C#', 'Python', 'Processing', '.net', 'PHP', 'Go', 'swift']
numbers = list(range(1, len(prog_lang) + 1))


def get_tuples_list(prog, nums):
    prog = list(map(lambda x: x.upper(), prog))
    tuples_list = list(zip(nums, prog))
    return tuples_list


def filtered_tuples(tuples_list):
    new_tuples = []
    for index, name in tuples_list:
        score_sum = reduce(lambda x, y: x + ord(y), name, 0)
        if (score_sum % index == 0):
            new_tuples.append((score_sum, name))
    return new_tuples


x = get_tuples_list(prog_lang, numbers)
print(x)
print(filtered_tuples(x))
