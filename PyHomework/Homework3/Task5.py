# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа


with open('text5', 'r') as data:
    numbers = data.readlines()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])


def odd_numbers(numbers):
    odd_num = []
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            odd_num.append(numbers[i])
    return odd_num


print(numbers)
x = odd_numbers(numbers)
print(x)

with open('text6', 'w') as data:     #Здесь немного отошел от условия, запись производится в другой файл, чтобы можно было посмотреть исходный файл с числами.
    for i in range(len(x)):
        data.writelines(str(x[i])+"\n")

# with open('text5', 'w') as data:  #Для записи новых значений в исходный файл
#     for i in range(len(x)):
#         data.writelines(str(x[i])+"\n")