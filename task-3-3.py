# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

camping_things = {'фонарь': 0.4,
                  'термос': 1.5,
                  'аптечка': 0.6,
                  'набор посуды': 1.3,
                  'предметы личной гигиены': 0.4,
                  'топорик': 1.4,
                  'телефон': 0.4,
                  'powerbank': 0.5,
                  'дождевик': 0.4,
                  'термобелье':0.5,
                  'коврик-пенка': 0.3,
                  'фляга': 1.5,
                  'компас': 0.1,
                  'нож': 0.4,
                  'саперная лопата': 1.3,
                  'спальник': 0.5,
                  'сухпаек': 2.8,
                  }
total = sum(camping_things.values())
max_weight = float(input(f'Введите максимальный вес рюкзака (от 5 до {(total - total * 0.15):.1f}): '))
weight = 0
kit_things = []
while weight <= max_weight:
    spam = max(camping_things, key=camping_things.get)
    kit_things.append(spam)
    eggs = camping_things.pop(spam)
    weight += eggs
kit_things.pop()
weight -= eggs
while weight <= max_weight:
    spam = min(camping_things, key=camping_things.get)
    kit_things.append(spam)
    eggs = camping_things.pop(spam)
    weight += eggs
kit_things.pop()
weight -= eggs
print(f'Комплект вещей -> {kit_things}\nВес комплекта -> {weight:.1f}')
