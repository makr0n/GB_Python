# Пользователь задаёт две строки.
# Определить количество вхождений одной строки в другой.


print("введите строку")
firststring = input()

print("введите строку")
secondstring = input()

count = secondstring.count(firststring)
print("The count is:", count)
