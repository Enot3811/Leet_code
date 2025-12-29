"""48. Rotate Image

https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


# Размышления
# Просто внимательно посмотреть как переносятся пиксели, что происходит с индексами.
# Оказывается, что во всех случаях используется всего 2 формулы
# i -> j
# j -> i где оно считается как len - 1 - j
# Преобразование будет удобно делать по "радиусам".
# То есть за итерацию крутить один слой.
# Можно взять по 4 зеркальных пикселя в каждой из сторон.

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for k in range(length // 2):
            for n in range(k, length - 1 - k):
                i = k
                j = n
                buff = matrix[i][j]

                for _ in range(3):
                    next_i = length - 1 - j
                    next_j = i
                    matrix[i][j] = matrix[next_i][next_j]
                    i = next_i
                    j = next_j

                matrix[i][j] = buff


if __name__ == '__main__':
    sol = Solution()
    matrices = [
        [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ],
        [
            [1,2],
            [3,4]
        ],
        [[1]],
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    ]
    for matrix in matrices:
        print(*matrix, sep='\n', end='\n\n')
        sol.rotate(matrix)
        print(*matrix, sep='\n', end='\n\n')
