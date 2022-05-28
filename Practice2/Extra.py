# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# x, y = 1, 20
#
#
# def delitel(n):
#     for i in range(2, 21):
#         if n % i != 0:
#             return False
#     return True
#
# x=20
# b= False
# while not b:
#     x+=20
#     b=delitel(x)
#     print(f'{x} {b}')
# print(x)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)     # integer division


d = 1
for i in range(2, 21): #last i=20
    d = lcm(d, i)

print (d)
