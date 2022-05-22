# Подсчитать сумму цифр в вещественном числе.

# x=3.54
# rt=str(x)
#
# str = rt
# print ("Исходная строка: " + str)
# res_str = str.replace('.', '')
# # Удаление всех 't'
# print("Строка после удаления всех символов t: " + res_str)
# tr=int(res_str)
# print(tr+1)

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





