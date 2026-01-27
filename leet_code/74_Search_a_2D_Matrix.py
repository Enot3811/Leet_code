"""74. Search a 2D Matrix

Check the image!
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""

# Теги
# Матрицы (Matrix)

# Размышления
# n-мерные массивы в си на самом деле те же одномерные.
# Вот и здесь представим, что это так.
# Просто реализуем бинарный поиск и будем конвертировать индексы.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        length = h * w
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // w
            j = mid % w
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

cases = [
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 70), False),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], -1), False),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 12), False),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1), True),
    (([[1]], 1), True),
    (([[1]], 2), False),
    (([[1,2,3,4,5]], 3), True),
    (([[1,2,3,5]], 3), True),
    (([[1,2,3,5]], 4), False),
]
sol = Solution()
for inp, ans in cases:
    res = sol.searchMatrix(*inp)
    print(inp, res, ans)
