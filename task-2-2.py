import math
from fractions import Fraction

def fract_sum(numerator1, denominator1, numerator2, denominator2):
    denominator = math.lcm(denominator1, denominator2)
    numerator = numerator1 * denominator / denominator1 + numerator2 * denominator / denominator2
    return short_fract(numerator, denominator)

def short_fract(numerator, denominator):
    com_divisor = 0
    while com_divisor != 1:
        com_divisor = math.gcd(int(numerator), int(denominator))
        numerator /= com_divisor
        denominator /= com_divisor
    return f'{int(numerator)}/{int(denominator)}'

def fract_multy(numerator1, denominator1, numerator2, denominator2):
    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    return short_fract(numerator, denominator)

num1 = input('Введите первую дробь в формате "a/b"(a-числитель, b-знаменатель): ').split('/')
num2 = input('Введите вторую дробь в формате "a/b"(a-числитель, b-знаменатель): ').split('/')
numerator1, denominator1 = int(num1[0]), int(num1[1])
numerator2, denominator2 = int(num2[0]), int(num2[1])
flag = input('Введите арифметическое действие 1 - сложение, 2 - умножение: ')
if flag == '1':
    print(f'Результат -> {fract_sum(numerator1, denominator1, numerator2, denominator2)}')
    print(f'Проверка ->  {Fraction(numerator1, denominator1) + Fraction(numerator2, denominator2)}')
elif flag == '2':
    print(f'Результат -> {fract_multy(numerator1, denominator1, numerator2, denominator2)}')
    print(f'Проверка ->  {Fraction(numerator1, denominator1) * Fraction(numerator2, denominator2)}')
