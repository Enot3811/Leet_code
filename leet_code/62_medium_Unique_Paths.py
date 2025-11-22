"""62. Unique Paths

Check the image!
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10**9.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways
to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
"""

# Размышления
# Можно решить в лоб: ветвление-рекурсия с кэшем.
# Получится n*m по сложности и n*m по памяти и в целом это и предел.
# Но можно сделать проще и лаконичнее.
# Эти пути - это по сути треугольник паскаля. Поэтому вместо рекурсий и стеков можем
# просто вычислить часть треугольника.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[1] * n] + [[1] + [0] * (n - 1)] * (m - 1)
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[-1][-1]

sol = Solution()
cases = [
    ((3,2), 3),
    ((2,3), 3),
    ((2,2), 2),
    ((1,2), 1),
    ((1,1), 1),
    ((3,7), 28),
    ((10, 4), 220)
]
for inp, ans in cases:
    res = sol.uniquePaths(*inp)
    print(inp, res, ans)
