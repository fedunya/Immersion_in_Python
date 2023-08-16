from random import randint

def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0' or int(num) > 1000:
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

num = randint(1, 1000)
print('Вас приветствует игра "Числовая угадайка"')
print('Я загадал число от 1 до 1000. Попробуй его отгадать за 10 попыток')
i = 10
flag = False
while i > 0:
    user_num = user_input(f'Осталось {i} попыток. Введите число от 1 до 1000: ')
    if user_num == num:
        flag = True
        break
    elif user_num > num:
        print('Слишком много, попробуйте еще раз')
        i -= 1
    else:
        print('Слишком мало, попробуйте еще раз')
        i -= 1
print('Поздравляю! Вы угадали число' if flag else 'Увы, попытки закончились. Вы проиграли')