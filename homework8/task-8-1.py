# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все
# вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle:
# - для дочерних объектов указывайте родительскую директорию;
# - для каждого объекта укажите файл это или директория;
# - для файлов сохраните его размер в байтах, а для директорий размер
#   файлов в ней с учётом всех вложенных файлов и директорий.

import os
from os.path import join, getsize
import json
import csv
import pickle

__all__ = ['get_size', 'dir_info']


def get_size(path):
    size = 0
    for dir_path, dir_name, file_name in os.walk(path):
        for name in file_name:
            file_path = join(dir_path, name)
            size += getsize(file_path)
    return size


def dir_info(path):
    list_info = []
    for dir_path, dir_name, file_name in os.walk(path):
        for dir in dir_name:
            dict_info = {'parent': dir_path}
            dict_info['name'] = dir
            dict_info['type'] = 'directory'
            dict_info['size'] = get_size(join(dir_path, dir))
            list_info.append(dict_info)
        for file in file_name:
            dict_info = {'parent': dir_path}
            dict_info['name'] = file
            dict_info['type'] = 'file'
            dict_info['size'] = getsize(join(dir_path, file))
            list_info.append(dict_info)
    with open('dir_info.json', 'w') as f:
        json.dump(list_info, f)
    with open('dir_info.csv', 'w', encoding="UTF-8", newline='') as f:
        writer = csv.DictWriter(f, dialect='excel', fieldnames=list_info[0].keys())
        writer.writeheader()
        writer.writerows(list_info)
    with open("dir_info.pickle", "wb") as f:
        pickle.dump(list_info, f)
    return list_info


if __name__ == '__main__':
    info = dir_info(os.getcwd())
    print(*info, sep='\n')

