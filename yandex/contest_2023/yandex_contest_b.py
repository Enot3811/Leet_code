"""
Даётся картинка с масками объектов (единицы в нулевой матрице).
Необходимо посчитать количество объектов при том, что они не сливаются.
Могут соседствовать по диагонали, но не вертикали-горизонтали.
"""

import numpy as np


def print_matrix(matrix):
    h = matrix.shape[0]
    for i in range(h):
        print(' '.join(map(str, matrix[i])))


with open('input.txt') as f:
    lines = f.readlines()

matrix = [list(map(int, line.split())) for line in lines]
matrix = np.array(matrix)
h, w = matrix.shape

bool_matrix = np.zeros_like(matrix, dtype=bool)
cat_counter = 1

stack = []
for i in range(h):
    for j in range(w):
        # Если ещё не обрабатывали этот пиксель
        # и нашли пиксель кота
        if not bool_matrix[i, j] and matrix[i, j] == 1:
            bool_matrix[i, j] = True

            # Добавляем соседей этой точки
            stack.append((i, j + 1))
            stack.append((i - 1, j))
            stack.append((i, j - 1))
            stack.append((i + 1, j))
            matrix[i, j] = cat_counter
            # Прорабатываем стек, пока он не закончится
            while len(stack) != 0:
                y, x = stack.pop()
                # Если точка находится в границах
                # и является котом
                # и мы её ещё не обрабатывали
                if (y >= 0 and y < h and x >= 0 and x < w) and matrix[y, x] == 1 and not bool_matrix[y, x]:
                    # То добавляем её соседей
                    stack.append((y, x + 1))
                    stack.append((y - 1, x))
                    stack.append((y, x - 1))
                    stack.append((y + 1, x))
                    bool_matrix[y, x] = True
                    matrix[y, x] = cat_counter
            cat_counter += 1

print(cat_counter - 1)
print_matrix(matrix)
