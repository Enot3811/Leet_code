"""986. Interval List Intersections

Check the images!
https://leetcode.com/problems/interval-list-intersections/

You are given two lists of closed intervals, firstList and secondList,
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x
with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty
or represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3]. 

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]],
secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= start_i < end_i <= 10**9
end_i < start_{i+1}
0 <= start_j < end_j <= 10**9 
end_j < start_{j+1}
"""

# Теги
# Интервалы (Intervals)

# Размышления
# Здесь помогает логика обнаружения пересечений из bboxes в детекции.
# Берём максимум из двух стартов и минимум из двух концов.
# То есть числа, которые тянутся к центру.
# Если оказывается, что старт больше конца, то пересечения нет.
# И таким образом просто перебираем пары у двух списков.
# Каждый раз оставляем тот элемент, у кого конец правее,
# так как он может ещё с кем-то пересечься.
# Двигаем тот, у кого конец левее.
# Для понимания всегда стоит порисовать отрезки.

from typing import List

class Solution:
    def intervalIntersection(
        self,
        firstList: List[List[int]],
        secondList: List[List[int]]
    ) -> List[List[int]]:
        i = 0
        j = 0
        intersections = []
        while i < len(firstList) and j < len(secondList):
            st1, end1 = firstList[i]
            st2, end2 = secondList[j]

            # Логика из bbox в детекции
            st_int = max(st1, st2)
            end_int = min(end1, end2)

            # Если есть пересечение
            if st_int <= end_int:
                intersections.append([st_int, end_int])

            # Двигаем того, у кого конец левее
            if end1 < end2:
                i += 1
            else:
                j += 1

        return intersections

sol = Solution()
cases = [
    (
        ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]),
        [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    ),
    (([[1,3],[5,9]], []), []),
    (
        ([[1,7],[9,9],[11,11]], [[2,3],[4,5],[6,6],[8,10]]),
        [[[2,3],[4,5],[6,6],[9,9]]]
    ),
    (([], []), []),
    (([[1,2],[2,3]],[[5,5],[6,7]]), [])
]
for inp, ans in cases:
    res = sol.intervalIntersection(*inp)
    print(inp, res, ans)
