# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def parser_file_path(file_path):
    file_folder, _, name_file = file_path.rpartition('\\')
    file_name, file_extension = name_file.split('.')
    return file_folder, file_name, file_extension

file_path = 'C:\Program Files\Common Files\System\DirectDB.dll'
print(parser_file_path(file_path))
