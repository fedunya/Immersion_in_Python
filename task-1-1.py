print('Введите стороны треугольника')
a, b, c = float(input('a = ')), float(input('b = ')), float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Такого треугольника не существует')
