"""253. Meeting Rooms II

Premium lock.
https://neetcode.io/problems/meeting-schedule-ii/

Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

# Размышления
# Задача выходит из Meeting Rooms (252), и можно её сразу решить, спроецировав
# решение той задачи на эту, тогда получится n^2.
# Но есть решение эффективнее, хотя и очень не интуитивное.
# Интуиция похожая на задачу с правильным расположением скобок.
# Когда скобка открывается, мы ждём, что она потом закроется. Счётчик открытых скобок +1
# Когда закрывается, то -1.
# Вот и здесь, если мы возьмём два массива: starts и ends, и будем проходить по ним
# одновременно с оглядкой на значение чисел, то проходя по starts будет +1 встреча,
# при проходе по ends -1.
# Просто следим, когда будет максимальное количество встреч.
# То есть они начались и идут одновременно.

from typing import List, Tuple

# Решение за nlog(n) (из-за сортировки, а так n)
class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int, int]]) -> int:
        starts = []
        ends = []
        for st, end in intervals:
            starts.append(st)
            ends.append(end)
        starts.sort()
        ends.sort()
        st_idx = 0
        end_idx = 0
        num_meetings = 0
        ans = 0
        # Проходим по обоим массивам одновременно. Берём min(starts[i], ends[j])
        while st_idx < len(starts):
            if starts[st_idx] < ends[end_idx]:
                num_meetings += 1
                st_idx += 1
            else:
                ans = max(ans, num_meetings)
                num_meetings -= 1
                end_idx += 1
        ans = max(ans, num_meetings)
        return ans


# # Решение в лоб за n^2
# class Solution:
#     def minMeetingRooms(self, intervals: List[Tuple[int, int]]) -> int:
#         intervals.sort(key=lambda x: x[0])
#         boundaries = [0,]
#         for interval in intervals:
#             # Проходим по дням
#             for i, bound in enumerate(boundaries):
#                 # Смотрим, можем ли добавить в текущий день
#                 if bound <= interval[0]:
#                     # Если да, то теперь новая встреча крайняя.
#                     # Обновляем день, прекращаем поиск дня
#                     boundaries[i] = interval[1]
#                     break
#             # Если прошли по всем дням и никуда не пристроили, то делаем новый
#             else:
#                 boundaries.append(interval[1])
#         return len(boundaries)


cases = [
    ([(0,30),(5,10),(15,20)], 2),
    ([(5,8),(9,15)], 1),
    ([(0,4),(6,9),(20,22),(5,5),(9,9),(9,15)], 1),
    ([(0,4),(6,9),(20,22),(5,5),(9,10),(9,15)], 2),
    ([(0,4),(3,6),(5,6),(5,6),(6,8),(7,9)], 3),
    ([(0,3),(1,6),(6,7),(4,10)], 2),
]
sol = Solution()
for intervals, ans in cases:
    res = sol.minMeetingRooms(intervals)
    print(intervals, res, ans)