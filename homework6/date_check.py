# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
from datetime import datetime as dt
import calendar

__all__ = ['check_date', 'check_leap']
YEARS = range(1, 10_000)


def check_date(date_for_check):
    try:
        _ = dt.strptime(date_for_check, "%d.%m.%Y").date()
        return True
    except ValueError:
        return False


def check_leap(date_for_check):
    if calendar.isleap(int(date_for_check.split(".")[-1])):
        return 'Год високосный'
    else:
        return 'Год невисокосный'


if __name__ == '__main__':
    if len(argv) > 1:
        _, *arguments = argv
        date_for_check = arguments[0]
        if int(date_for_check.split(".")[-1]) in YEARS and check_date(date_for_check):
            print(dt.strptime(date_for_check, "%d.%m.%Y").date(), check_leap(date_for_check))
        else:
            print('Дата указана не корректно')
    else:
        print('Вы не указали дату для проверки')

