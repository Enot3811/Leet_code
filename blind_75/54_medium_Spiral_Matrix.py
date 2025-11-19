"""54. Spiral Matrix

Check the images!
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


# Размышления
# Задачу можно решить много как, но наиболее лаконичный вариант с отслеживанием
# текущих границ матрицы.
# То есть, например, мы прошли по верхней стороне слева-направо и сделали top+=1.
# И когда будем идти наверх, то упрёмся в изменённый top.
# Будем крутить круги до тех пор, пока какие-то из двух границ не упрутся друг в друга.
# И если присмотреться, то это условие и означает, что мы перечислили все числа

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Проверки, так как на нечётных могли упереться ещё до конца круга,
            # и тогда цикл отправит элементы обратно
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


sol = Solution()
cases = [
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ],
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [[1]],
    [[1,2]],
    [[1],[2]],
    [
        [1,2],
        [3,4]
    ],
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18]
    ],
    [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12],
        [13,14,15]
    ],
    [
        [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24]
    ],
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ],
    [
        [1,2,3,4,5],
        [6,7,8,9,10]
    ]
]

for matrix in cases:
    print(*matrix, sep='\n')
    print(sol.spiralOrder(matrix), end='\n\n')
