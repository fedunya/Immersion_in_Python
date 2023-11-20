# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import logging
import argparse
from datetime import datetime as dt
import calendar

__all__ = ['check_date', 'check_leap']
YEARS = range(1, 10_000)

logging.basicConfig(filename='log.log.', filemode='w', encoding='utf-8', 
                    format='{asctime} {levelname} {lineno}: {msg}', style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


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
    parser = argparse.ArgumentParser(description='Checking the correctness of the date')
    parser.add_argument('date', metavar='DD.MM.YYYY', type=str, 
                        nargs='?', help='press date for check')
    args = parser.parse_args()
    if args.date != None:
        if int(args.date.split(".")[-1]) in YEARS and check_date(args.date):
            print(dt.strptime(args.date, "%d.%m.%Y").date(), check_leap(args.date))
        else:
            print('Дата указана не корректно')
    else:
        print('Вы не указали дату для проверки')