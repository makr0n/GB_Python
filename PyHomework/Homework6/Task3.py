# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите.
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть.
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.


alphabet = 'abcdefghijklmnopqrstuwxyz'
key = 13


def rot_encoding(message, key):
    encoded = ''
    for item in message.lower():
        if item in alphabet:
            encoded += alphabet[(alphabet.find(item) + key) % len(alphabet)]
        else:
            encoded += item
    return encoded


def decoding(text, key):
    decoded = ''
    for item in text:
        if item in alphabet:
            x = alphabet.find(item)
            decoded += alphabet[(alphabet.find(item) - key) % len(alphabet)]
        else:
            decoded += item
    return decoded


text = '^Parabellum* '
print(text)
enc = rot_encoding(text, key)
print(enc)
dec = decoding(enc, key)
print(dec)
