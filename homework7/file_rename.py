# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени
# добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только
# для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся
# буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
# если оно передано. Далее счётчик файлов и расширение.

from pathlib import Path

__all__ = ['files_rename']


def files_rename(new_name: str, ext: str, /, range_save=(0, 0), *, count_digits=1, new_ext=None):
    count = 0
    p = Path(Path().cwd())
    if new_ext is None:
        new_ext = ext
    for obj in p.iterdir():
        # print(obj)
        if obj.is_file() and obj.suffix == ext:
            obj.rename(f'{obj.stem[range_save[0]:range_save[1]]}{new_name}{count:0>{count_digits}}{new_ext}')
        count += 1
    return count


if __name__ == '__main__':
    count_files = files_rename('new', '.gb', (0, 4), count_digits=3)
    print(f'Переименовано {count_files} файлов')