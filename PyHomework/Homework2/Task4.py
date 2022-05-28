# Написать программу преобразования десятичного числа в двоичное

def decimal_to_binary(decimal_number):
    binary = []
    while decimal_number > 0:
        binary.append(decimal_number % 2)
        decimal_number //= 2
    # binary.reverse()
    # return(binary)

    new_bin = []
    for i in range(len(binary)):  # Полученные значения записаны в обратном порядке, необходимо развернуть список
        new_bin.append(binary[len(binary) - i - 1])

    return (new_bin)


binary = decimal_to_binary(20)
print(binary)


# Написать программу преобразования двоичного числа в десятичное

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += binary[i] * (2 ** (len(binary) - i - 1))
    return decimal


decimal=binary_to_decimal(binary)
print(decimal)
