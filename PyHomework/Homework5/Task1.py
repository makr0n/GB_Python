# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

origin_text = 'абвгдеж рабав копыто фабв Абкн АБВ абрыволк аБволк АБоапапВ'


# def exluding_typos(origin_text):
#     origin_text = list(filter(lambda s: 'абв' not in s, origin_text.split()))
#     return " ".join(origin_text)
#
# new_text = exluding_typos(origin_text)
# print(new_text)

def delete(text):
    new_text = list(filter(lambda x: x.lower().find('абв') == -1, text.split()))
    return " ".join(new_text)


print(delete(origin_text))
