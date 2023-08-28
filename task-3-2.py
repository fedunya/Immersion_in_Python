# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

import string

with open('task-3-2.txt', encoding='utf-8') as data:
    my_str = data.read()

my_list = [i.strip(string.punctuation).lower() for i in my_str.split()]
my_set = set(my_list)
my_dict = {key: my_list.count(key) for key in my_set}
print('10 самых часто встречаемых слов в статье:')
for i in range(10):
    spam = max(my_dict, key=my_dict.get)
    eggs = my_dict[spam]
    my_dict.pop(spam)
    print(f'{i + 1:>2}. {spam:<10} -> {eggs:>3} раз.')
