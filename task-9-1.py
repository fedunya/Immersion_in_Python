from random import randint
import csv
import json

CSV_FILE = 'input_data.csv'
JSON_FILE = 'results.json'

# Min, max количество строк csv-файла
MIN_ROWS = 100
MAX_ROWS = 1000

# Диаппазон коэффициентов квадратного уравнения
MIN_COEF = -100
MAX_COEF = 100

# Кол-во коэффициентов
COUNT_COEF = 3


def generate_csv_file(file_name, rows):
    if not MIN_ROWS <= rows <= MAX_ROWS: # для дебильных автотестов GeekBrains
        rows = randint(MIN_ROWS, MAX_ROWS) # эту проверку убираем
    data = []
    for _ in range(rows):
        data.append([randint(MIN_COEF, MAX_COEF) for i in range(COUNT_COEF)])
    with open(file_name, "w", encoding="UTF-8", newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(data)


def save_to_json(func):
    def wrapper(*args, **kwargs):
        with open(CSV_FILE, "r", encoding="UTF-8") as f:
            csv_reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            r = []
            for row in csv_reader:
                res_json = {}
                res_json['a'], res_json['b'], res_json['c'] = row
                solve = res_json['x1'], res_json['x2'] = func(row[0], row[1], row[2])
                r.append(res_json)
            with open(JSON_FILE, "w", encoding='UTF-8') as file:
                json.dump(r, file, indent=2)
        return solve
    return wrapper


@ save_to_json
def find_roots(a, b, c):
    x1 = x2 = None
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
    elif d == 0:
        x1 = x2 = -b / 2 * a
    return x1, x2


if __name__ == '__main__':
    generate_csv_file(CSV_FILE, 100)
    find_roots()
    print(True)