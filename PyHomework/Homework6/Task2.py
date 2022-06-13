# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги,а втором файлике — сжатая версия этого текста).

def rl_encoding(raw_data, encoded_data):
    with open(raw_data, 'r') as raw:
        for item in raw:
            raw_str = ''.join(str(item))
    encoded = ''
    i = 0
    while (i <= len(raw_str) - 1):
        count = 1
        symbol = raw_str[i]
        j = i

        while (j < len(raw_str) - 1):
            s = j
            x = raw_str[j]
            c = raw_str[j + 1]
            if (raw_str[j] == raw_str[j + 1]):
                count += 1
                j += 1
            else:
                break
        encoded += str(count) + symbol
        i = j + 1
    with open(encoded_data, 'w') as enc:
        enc.write(encoded)


def rl_decoding(encoded_data, decoded_data):
    with open(encoded_data, 'r') as enc:
        for item in enc:
            txt = ''.join(str(item))
    decoded = ''
    i = 0
    j = 0
    while (i <= len(txt) - 1):
        if(i<len(txt)):
            count = int(txt[i])
            word = txt[i + 1]
            for j in range(count):
                decoded += word
                j = j + 1
            i = i + 2
    with open(decoded_data, 'w') as f:
        f.write(decoded)



rl_encoding('Text_origin', 'Text_encoded')
rl_decoding('Text_encoded', 'Text_decoded')
