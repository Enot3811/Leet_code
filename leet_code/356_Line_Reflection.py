"""356. Line Reflection

Premium lock. Check the images!
https://leetcode.doocs.org/en/lc/356/

Given n points on a 2D plane, find if there is such a line parallel to the y-axis
that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line
that after reflecting all points over the given line,
the original points' set is the same as the reflected ones.

Note that there can be repeated points.

Example 1:
Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.

Example 2:
Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can't choose a line.

Constraints:
n == points.length
1 <= n <= 10**4
-10**8 <= points[i][j] <= 10**8

Follow up: Could you do better than O(n2)?
"""

# Теги
# Поиск в сете (set search)

# Размышления
# Первая мысль, которая может прийти, это отсортировать точки по X,
# чтобы они попарно распределились слева и справа.
# Но в этом способе есть проблема, что Y не распределятся попарно.
# Например, [[-1,1],[-1,2],[1,1],[1,2]], хоть сортируй, хоть не сортируй Y,
# всё равно в пару (-1,1) может попасть (1,2).
# К тому же в условии говорилось про дубликаты.
# Правильная мысль - использовать сет.
# Сет позволит как избавиться от дубликатов, так и быстро проверять наличие пары
# у текущей точки.
# Так же, как и в первом способе, находим 2 крайние точки, считаем ось симметрии,
# но теперь не попарно сравниваем левую и правую, а проходим по точкам,
# и ищем в сете их правильную симметрию.
# Если её нет, то всё.

from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if len(points) == 1:
            return True
        # Превращаем точки в сет, чтобы удобно искать пару
        points = set(map(tuple, points))
        # Находим две крайние точки, считаем ось симметрии
        left_p = min(*points, key=lambda p: p[0])
        right_p = max(*points, key=lambda p: p[0])
        mid = (left_p[0] + right_p[0]) // 2

        for p in points:
            # Вычисляем симметричную точку
            sim_p = (mid - p[0], p[1])
            if sim_p not in points:
                return False
        # Проверили все точки
        return True

cases = [
    ([[1,1],[-1,1]], True),
    ([[1,1],[-1,-1]], False),
    ([[5,1],[-5,1],[3,2],[-3,2],[0,0]], True),
    ([[1,1]], True),
    ([[2,1],[4,1],[10,-4],[-4,-4]], True),
    ([[5,1],[-5,1],[3,2],[-3,2]], True),
    ([[5,1],[-5,1],[3,1],[-3,2],[0,0]], False),
    ([[5,1],[-5,1],[-3,2],[0,0]], False),
    ([[-1,1],[-1,2],[1,1],[1,2]], True),
    ([[1,1], [1,1], [-1,1]], True)
]
sol = Solution()
for points, ans in cases:
    res = sol.isReflected(points)
    print(points, res, ans)
