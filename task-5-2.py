# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


def size_premium(staff, salaries, bonuses):
    return {employee: salary * float(bonus[:-1]) / 100
            for employee, salary, bonus in zip(staff, salaries, bonuses)}


staff = ['Ivan', 'Petr', 'Anton']
salaries = [50_000, 70_000, 100_000]
bonuses = ['10.5%', '8.5%', '5.5%']
print(staff, salaries, bonuses, size_premium(staff, salaries, bonuses), sep='\n')