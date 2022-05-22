"""
2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

    Примеры:

    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
"""

"""
firstNum = int (input("Введите первое число: "))
secondNum = int (input("Введите второе число: "))
thirdNum = int (input("Введите третье число: "))
fourthNum = int (input("Введите четвертое число: "))
fifthNum = int (input("Введите пятое число: "))
maxNum=firstNum

if secondNum > maxNum: maxNum = secondNum
if thirdNum > maxNum: maxNum = thirdNum
if fourthNum > maxNum: maxNum = fourthNum
if fifthNum > maxNum: maxNum = fifthNum

print(maxNum) 
"""

numbers = []
for i in range(5):
    numbers.append(int(input(f'Введите число {i+1}: ')))

maxNumber = numbers[0]
for i in numbers:
    if i > maxNumber: 
        maxNumber = i
print(maxNumber)

