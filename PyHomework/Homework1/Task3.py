# Подсчитать сумму цифр в вещественном числе.

def sumfloatnumbers(number):
    number = str(number)
    newstr = number.replace('.', '')
    sum = 0
    number = int(newstr)
    while (number != 0):
        sum = sum + number % 10
        number = number // 10
    return sum

print("Введите натуральное число:",end="")
number=float(input())
print(sumfloatnumbers(number))





