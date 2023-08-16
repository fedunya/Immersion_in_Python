def user_input(a):
    num = input(a)
    while not num.isdigit() or num == '0' or int(num) > 100000:
        print('Неверный ввод, повторите!')
        num = input(a)
    num = int(num)
    return num

num = user_input('Введите натуральное число от 1 до 100000: ')
i = 2
flag = False
while i**2 <= num:
    if num % i == 0:
        flag = True
        break
    else: i += 1
print('Число составное' if flag else 'Число простое')