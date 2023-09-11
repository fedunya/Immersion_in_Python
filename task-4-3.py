# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from decimal import Decimal

MIN_SUM_TAX = Decimal('5000000')
TAX_PERCENTAGE = Decimal('0.10')
BONUS_COUNT = 3
BONUS_PERCENTAGE = Decimal('0.03')
MULTIPLICITY = 50
MIN_PERCENT = 30
MAX_PERCENT = 600
WITHDRAW_PERCENTAGE = Decimal('0.015')


def menu(balance):
    show_balance(balance)
    print('Введите цифру требуемого действия:', 
          '0 - выход', '1 - пополнить счет', '2 - снять со счета', sep='\n')
    res = user_input('-> ', 0)
    return res


def show_balance(balance):
    print('БАЛАНС ВАШЕГО СЧЕТА ->', balance.quantize(Decimal("1.00")))


def main():
    list_transactions = list()
    count_transactions = 0
    balance = Decimal('0.00')
    action = int(menu(balance))
    while action != 0:
        if balance >= MIN_SUM_TAX:
            balance -= balance * TAX_PERCENTAGE
        if action == 1:
            balance, count_transactions, list_transactions = deposit(balance, count_transactions, list_transactions)
            print('Операция пополнения завершена')
            if count_transactions % BONUS_COUNT == 0:
                balance += balance * BONUS_PERCENTAGE
            action = int(menu(balance))
        elif action == 2:
            balance, count_transactions, list_transactions = withdraw(balance, count_transactions, list_transactions)
            
            if count_transactions % BONUS_COUNT == 0:
                balance += balance * BONUS_PERCENTAGE
            action = int(menu(balance))
    show_balance(balance)
    print('Вы завершили сеанс работы. До свидания!')
    print(list_transactions)


def user_input(message, input_index):
    flag = True
    if input_index == 0:
        while flag:
            action = input(message)
            if action in '012':
                flag = False
            else:
                print('Не верно! Введите цифру от 0 до 2', end=' ')
        return action
    elif input_index == 1:
        while flag:
            sum_deposit = input(message)
            if sum_deposit.isdigit():
                if int(sum_deposit) % MULTIPLICITY == 0:
                    flag = False
                else:
                    print('Сумма пополнения не кратна 50! Повторите ввод')
            else:
                print('Введено не число! Повторите ввод')
        return sum_deposit
    else:
        while flag:
            sum_withdraw = input(message)
            if sum_withdraw.isdigit():
                if int(sum_withdraw) % MULTIPLICITY == 0:
                    flag = False
                else:
                    print('Сумма пополнения не кратна 50! Повторите ввод')
            else:
                print('Введено не число! Повторите ввод')
        return sum_withdraw


def deposit(balance, count_transactions, list_transactions):
    show_balance(balance)
    print('Введите сумму для пополнения счета кратную 50')
    sum_deposit = Decimal(user_input('-> ', 1))
    balance += sum_deposit
    count_transactions += 1
    list_transactions.append(f'Пополнение {sum_deposit}')
    return balance, count_transactions, list_transactions


def withdraw(balance, count_transactions, list_transactions):
    show_balance(balance)
    print('Введите сумму для снятия со счета кратную 50')
    sum_withdraw = Decimal(user_input('-> ', 2))
    if sum_withdraw <= balance:
        balance -= sum_withdraw
        count_transactions += 1
        list_transactions.append(f'Снятие {sum_withdraw}')
        percent = sum_withdraw * WITHDRAW_PERCENTAGE
        if percent < MIN_PERCENT:
            balance -= MIN_PERCENT
        elif percent > MAX_PERCENT:
            balance -= MAX_PERCENT
        else:
            balance -= percent
        print('Операция снятия завершена')
    else:
        print('Сумма снятия превышает баланс')
    return balance, count_transactions, list_transactions


if __name__ == "__main__":
    main()