from random import randint

__all__ = ['check_placement', 'gen_placement']
COUNT_QUEENS = 8
SIZE_BOARD = 8


def check_placement(positions) -> bool:
    result = True
    for i in range(0, COUNT_QUEENS - 1):
        row1, col1 = positions[i]
        for j in range(i + 1, COUNT_QUEENS):
            row2, col2 = positions[j]
            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                result = False
                break
    return result


def gen_placement():
    positions = []
    for i in range(1, COUNT_QUEENS + 1):
        positions.append((i, randint(1, SIZE_BOARD)))
    return positions

if __name__ == '__main__':
    i = 1
    while i < 5:
        positions = gen_placement()
        if check_placement(positions):
            print(i, '->', positions)
            i += 1
