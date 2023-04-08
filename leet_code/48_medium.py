'''48. Rotate Image.'''


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
                next_i = length - 1 - j
                next_j = i
                matrix[i][j] = matrix[next_i][next_j]
                i = next_i
                j = next_j

                next_i = length - 1 - k
                next_j = i
                matrix[i][j] = matrix[next_i][next_j]
                i = next_i
                j = next_j

                next_i = length - 1 - j
                next_j = length - 1 - k
                matrix[i][j] = matrix[next_i][next_j]
                
                i = next_i
                j = next_j
                matrix[i][j] = buff


sol = Solution()
matrix = [[1, 2], [3, 4]]
print(*matrix, sep='\n')
sol.rotate(matrix)
print(*matrix, sep='\n')
