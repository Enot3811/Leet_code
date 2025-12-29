"""73. Set Matrix Zeroes

Check the images!
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0,
set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2**31 <= matrix[i][j] <= 2**31 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# Размышления
# Главная мысль, к которой надо прийти, это то, что нам надо помечать строки и столбцы
# на закрашивание во время прохода по матрице, и только потому уже их закрашивать.
# Для пометки можно использовать булевые списки размером n и m, и это уже неплохо.
# Однако предлагается сделать за нулевую память.
# Используем нулевой столбец и строку самой же матрицы для пометок, ведь всё равно
# исходные числа в этих столбцах/строках будут закрашены, если мы найдём ноль.
# Единственная проблема в элементе 0,0 , который принадлежит и строке и столбцу.
# Здесь просто добавим одну дополнительную переменную, чтобы не делить эту ячейку.

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero = False
        for i in range(len(matrix)):
            for j, num in enumerate(matrix[i]):
                if num == 0:
                    if i == 0:
                        row_zero = True
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        # Не закрасить пометки для столбцов
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        # Можно всё закрасить, так как строки уже прошли
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        # нулевая строка, закраска пометок столбцов
        if row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0


sol = Solution()
cases = [
    (
        [
            [1,1,1],
            [1,0,1],
            [1,1,1]
        ],
        [
            [1,0,1],
            [0,0,0],
            [1,0,1]
        ]
    ),
    (
        [
            [0,1,2,0],
            [3,4,5,2],
            [1,3,1,5]
        ],
        [
            [0,0,0,0],
            [0,4,5,0],
            [0,3,1,0]
        ]
    ),
    (
        [
            [1,1,0,1,1,0],
            [1,1,1,1,1,1],
            [0,1,1,1,1,1],
            [1,1,1,1,0,1],
            [0,0,1,1,1,1],
        ],
        [
            [0,0,0,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
        ]
    ),
    (
        [
            [0]
        ],
        [
            [0]
        ]
    ),
    (
        [
            [1]
        ],
        [
            [1]
        ]
    ),
    (
        [
            [1,2,3,4],
            [5,0,7,8],
            [0,10,11,12],
            [13,14,15,0]
        ],
        [
            [0,0,3,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
    )
]
for matrix, ans in cases:
    print(*matrix, sep='\n', end='\n\n')
    sol.setZeroes(matrix)
    print(*matrix, sep='\n', end='\n\n')
    print(*ans, sep='\n', end='\n\n')
        