# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = 5
sum = 0
posl = []
for i in range(1, n + 1):
    posl.append((1 + 1 / i) ** i)
    sum += posl[i - 1]

print(posl)
print(sum)
