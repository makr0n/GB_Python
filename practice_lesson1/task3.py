"""
1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

    *Примеры:*

    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
"""
print('Введите число:')
number=abs(int(input()))
print()
my_list=[]
for i in range (-number,number+1):
    my_list.append(i)

print(my_list)
    