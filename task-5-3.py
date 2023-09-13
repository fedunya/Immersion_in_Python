# Создайте функцию генератор чисел Фибоначчи


def fibonacci_numbers(n):
    num1, num2 = 0, 1
    if n > 0:
        for i in range(0, n):
            yield num1
            num1, num2 = num2, num1 + num2
    elif n < 0:
        for i in range(0, -n):
            yield num1
            num1, num2 = num2, num1 - num2
    else:
        yield num1     


print(*fibonacci_numbers(12))