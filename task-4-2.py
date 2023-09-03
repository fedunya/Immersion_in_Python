# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.


def create_dict(**kwars):
    """The function creates a dictionary of key arguments and their values"""
    my_dict = {}
    for k, v in kwars.items():
        try:
            _ = hash(v)
            my_dict[v] = k
        except TypeError:
            my_dict[str(v)] = k
    return my_dict


my_dict = create_dict(first=1, second=2, third=3, forth=[4,])
print('Аргументы: first=1, second=2, third=3, forth=[4,]')
print(f'dict -> {my_dict}')