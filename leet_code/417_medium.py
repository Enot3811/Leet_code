"""417. Pacific Atlantic Water Flow

Check images!
https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean
and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells
directly north, south, east, and west if the neighboring cell's height is less than
or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans. 

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans,
as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow
to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10**5
"""

# Размышления
# Сразу приходит в голову поиск в глубину с кэшированием, но такое решение в лоб
# будет весьма сложным в реализации, хотя и не таким плохим по скорости.
# Будут проблемы с обозначением тупиков (ячеек, которые не дошли до океана),
# возможно понадобится несколько сетов или булевая матрица, с которой совсем
# неудобно работать.
# Одна очень простая мысль, которая сильно упрощает задачу:
# Зачем идти сверху вниз, перебирая все-все ячейки и тыкаться в тупики, если
# можно пойти снизу вверх только от тех немногих ячеек, которые по краям грида,
# и никогда не заходить в тупики, а просто идти в те ячейки, которые выше.
# Тогда нам нужен всего лишь один сет, в который мы просто кладём ячейки,
# по которым прошли. А все те, в которые мы не смогли прийти, априори не подходят.



from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = len(heights)
        w = len(heights[0])

        pacific_set = set(
            [(i, 0) for i in range(h)] +
            [(0, i) for i in range(w)]
        )
        atlantic_set = set(
            [(i, w - 1) for i in range(h)] +
            [(h - 1, i) for i in range(w)]
        )
        for current_set in (pacific_set, atlantic_set):
            stack = list(current_set)
            while len(stack) != 0:
                i, j = stack.pop()
                # Вверх
                if (i > 0 and (i - 1, j) not in current_set and heights[i][j] <= heights[i - 1][j]):
                    current_set.add((i - 1, j))
                    stack.append((i - 1, j))
                # Вниз
                if (i < h - 1 and (i + 1, j) not in current_set and heights[i][j] <= heights[i + 1][j]):
                    current_set.add((i + 1, j))
                    stack.append((i + 1, j))
                # Влево
                if (j > 0 and (i, j - 1) not in current_set and heights[i][j] <= heights[i][j - 1]):
                    current_set.add((i, j - 1))
                    stack.append((i, j - 1))
                # Вправо
                if (j < w - 1 and (i, j + 1) not in current_set and heights[i][j] <= heights[i][j + 1]):
                    current_set.add((i, j + 1))
                    stack.append((i, j + 1))
        return list(
            map(list, pacific_set.intersection(atlantic_set)))


sol = Solution()
tests = [
    ([
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]],
        [
            [0, 4],
            [1, 3],
            [1, 4],
            [2, 2],
            [3, 0],
            [3, 1],
            [4, 0]
        ]
    ),
    ([
        [9, 9, 9, 9, 9],
        [1, 2, 3, 4, 9],
        [9, 9, 9, 5, 9],
        [9, 8, 7, 6, 9]],
        [[0,0],[0,1],[0,2],[0,3],[0,4],[1,4],[2,0],[2,1],[2,2],[2,4],[3,0],[3,1],[3,2],[3,3],[3,4]]
    )
]
for grid, ans in tests:
    res = sol.pacificAtlantic(grid)
    print(grid, res, ans, sep='\n', end='\n\n')
