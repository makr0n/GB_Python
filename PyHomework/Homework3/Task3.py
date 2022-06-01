# Составить список простых множителей натурального числа N
from random import randint

def simple_mult(n):
   i = 2
   simple_mult = []
   while i * i <= n:
       while n % i == 0:
           simple_mult.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       simple_mult.append(n)
   return simple_mult

rand=randint(0,170)
print(f'Список простых множителей числа {rand}: {simple_mult(rand)}')