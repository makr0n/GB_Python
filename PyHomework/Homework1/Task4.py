"""Написать программу получающую набор произведений чисел от 1 до N.
Пример: пусть N = 4, тогда
[ 1, 2, 6, 24 ]"""


def numericsequence(number):
    sequence = []
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
        sequence.append(factorial)
    return sequence


print("Введите число:", end="")
number = int(input())
print(numericsequence(number))
