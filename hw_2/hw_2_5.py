# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
# заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def ascii_codes(start, end):
    str = f'{start}=>{chr(start)}'  # чтобы не было лишних пробелов
    if end - start < 10:
        for i in range(start + 1, end + 1):
            str = f'{str}    {i}=>{chr(i)}'
        return str
    else:
        for i in range(start + 1, start + 10):
            str = f'{str}    {i}=>{chr(i)}'
        return str + '\n' + ascii_codes(start + 10, end)


start_num = 32
end_num = 127
res = ascii_codes(start_num, end_num)

print(f'{res}')
