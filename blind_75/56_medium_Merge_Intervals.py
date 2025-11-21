"""56. Merge Intervals

https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Constraints:
1 <= intervals.length <= 10**4
intervals[i].length == 2
0 <= starti <= endi <= 10**4
"""

# Размышления
# Отсортируем интервалы, чтобы они шли по порядку, а дальше мы легко можем смотреть,
# сливаются ли интервалы или нет по их стартовому и конечному значению


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0].copy()]
        for curr_st, curr_end in intervals:
            prev_end = merged[-1][1]
            if curr_st <= prev_end:
                merged[-1][1] = max(prev_end, curr_end)
            else:
                merged.append([curr_st, curr_end])
        return merged


sol = Solution()
cases = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[4,7],[1,4]], [[1,7]]),
    ([[0,1], [1,2], [2,3],[3,4],[4,5]], [[0,5]]),
    ([[1,2],[2,3],[3,4],[1,3]], [[1,4]]),
    ([[1,2]], [[1,2]]),
    ([[0,2],[0,5],[1,2],[3,5],[5,6]], [[0,6]]),
    ([[1,2],[1,2],[1,2]], [[1,2]]),
    ([[1,3],[2,4],[3,5],[3,6]], [[1,6]]),
    ([[0,7],[0,3],[0,5],[2,4],[3,7],[4,6],[4,5]], [[0,7]]),
    ([[0,7],[5,6],[1,3],[9,10],[10,10],[4,5],[6,8]], [[0,8],[9,10]]),
    ([[0,0],[1,1],[2,2],[2,4],[3,3],[5,7],[8,8]], [[0,0],[1,1],[2,4],[5,7],[8,8]]),
    ([[1,1]], [[1,1]])
]
for intervals, ans in cases:
    res = sol.merge(intervals)
    print(intervals, res, ans)
