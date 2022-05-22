"""Написать программу получающую набор произведений чисел от 1 до N.
Пример: пусть N = 4, тогда
[ 1, 2, 6, 24 ]"""

def numericsequence(number):
    sequence = [1]
    for i in range(1, number):
        sequence.append(sequence[i-1]*(i+1))
    return sequence

print("Введите число:",end="")
number=int(input())
print(numericsequence(number))



