def hexadecimal(num):
    hex_digits = '0123456789abcdef'
    res = ''
    while num > 0:
        remainder = num % 16
        res += hex_digits[remainder]
        num = num // 16
    return res[::-1]

num = int(input('Введите целое число: '))
if num < 0:
    minus = '-'
else: minus = ''
print(f'Результат -> {minus}0x{hexadecimal(abs(num))}\nПроверка  -> {hex(num)}')
