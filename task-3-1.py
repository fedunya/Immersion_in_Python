# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 1, 7, 4, 3, 9, 6, 8, 8, 4, 5, 7]
my_set = set(my_list)
new_list = []
for i in my_set:
    if my_list.count(i) > 1:
        new_list.append(i)

print(new_list)
