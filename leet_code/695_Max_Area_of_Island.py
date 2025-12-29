"""695. Max Area of Island

Check the image!
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

# Теги
# Продолжение задачи, Поиск в глубину (dfs)

# Размышления
# Задача является прямым продолжением (200. Number of Islands).
# Мы можем находить острова с помощью алгоритма закраски (dfs с пометками).
# Только теперь помимо самой закраски будем ещё считать количество сегментов,
# как 1 + соседи.
# А сам dfs запускать, только если текущий сегмент = 1.

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h_grid = len(grid)
        w_grid = len(grid[0])

        def dfs(i: int, j: int) -> int:
            directions = [-1, 0, 1, 0, -1]
            ans = 1
            grid[i][j] = -1  # помечаем уже пройденные участки, чтобы не повторяться
            for k in range(4):
                # 4 направления
                di = i + directions[k]
                dj = j + directions[k + 1]
                if 0 <= di < h_grid and 0 <= dj < w_grid and grid[di][dj] == 1:
                    ans += dfs(di, dj)  # текущий + что насобирают соседи
            return ans

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
        

cases = [
    ([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ], 6),
    ([
        [0,0,0,0,0,0,0,0]
    ], 0),
    ([
        [1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,1],
        [1,0,1,0,0,1,0,1],
        [1,0,1,0,1,1,0,1],
        [1,0,1,1,0,1,0,1],
        [1,0,1,0,0,1,0,1],
        [1,0,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,1],
        [1,1,1,0,1,1,1,1],
    ], 31),
    ([
        [1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,1],
        [1,0,1,1,0,1,0,1],
        [1,0,1,0,1,1,0,0],
        [1,0,1,1,1,1,0,1],
        [0,0,1,1,0,1,0,1],
        [1,0,1,1,1,1,0,1],
        [1,0,0,1,0,0,0,1],
        [1,1,1,0,1,1,1,1],
    ], 22),
    ([[0]], 0),
    ([[1]], 1)
]
sol = Solution()
for grid, ans in cases:
    res = sol.maxAreaOfIsland(grid)
    print(res, ans)
