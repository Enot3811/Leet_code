"""435. Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove
to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping.
For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2]
to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals
since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 10**5
intervals[i].length == 2
-5 * 10**4 <= starti < endi <= 5 * 10**4
"""


# Размышления
# Интуитивно сразу хочется отсортировать отрезки, чтобы можно было как-то разумнее
# на них смотреть.
# Как определять пересекаются ли два отрезка тоже понятно, смотрим на конец первого
# и начало второго.
# Главная мысль, толкающая к решению. Какие отрезки надо удалять?
# Нужно ли искать отрезок с наибольшим количеством пересечений?
# Или удалять самые длинные с пересечениями?
# Ответ: при пересечении нам в любом случае нужно удалить один из двух уже сразу.
# Какой из них? Тот, у которого конец правее. У него больше вероятность пересечения
# со следующими отрезками.
# В итоге проходим по отрезкам, смотрим пересечения текущего и предыдущего.
# Если у предыдущего коне правее, то удаляем его. Если у текущего, то его.
# |-------| |---|
#       |---|
#
# |-------| |---|
#    |---|

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[0])  # Ускоряем сортировку
        # В целом, нам без разницы в каком порядке пойдут конечные значения,
        # ведь мы всё равно сравниваем концы и сохраняем тот, который меньше

        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            curr_st, curr_end = intervals[i]
            # Есть пересечение
            if curr_st < prev_end:
                ans += 1
                # Оставляем конец, который меньше
                prev_end = min(prev_end, curr_end)
            else:
                prev_end = curr_end
        return ans
            

sol = Solution()
cases = [
    ([[0,1], [1,2], [2,3],[3,4],[4,5]], 0),
    ([[1,2],[2,3],[3,4],[1,3]], 1),
    ([[1,2]], 0),
    ([[0,2],[0,5],[1,2],[3,5],[5,6]], 2),
    ([[1,2],[1,2],[1,2]],2),
    ([[1,3],[2,4],[3,5],[3,6]],2),
    ([[0,7],[0,3],[0,5],[2,4],[3,7],[4,6],[4,5]], 5)
]
for intervals, ans in cases:
    res = sol.eraseOverlapIntervals(intervals)
    print(intervals, res, ans)
