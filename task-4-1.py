# Напишите функцию для транспонирования матрицы.


def transpon(m):
    """The function transposes the input matrix"""
    trans_matrix = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return trans_matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(*matrix, sep='\n', end='\n\n')
trans_matrix = transpon(matrix)
print(*trans_matrix, sep='\n')