"""57. Insert Interval

https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals
where intervals[i] = [starti, endi] represent the start and the end of the ith interval
and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order
by starti and intervals still does not have any overlapping intervals
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place.
You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10**4
intervals[i].length == 2
0 <= starti <= endi <= 10**5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10**5
"""

# Теги
# Интервалы (Intervals)

# Размышления
# Рассмотрим все варианты
# 1
# |----|
#        |--|
# 2
# |----|
#     |--|
# 3     
# |----|
#  |--|
# 4
#   |----|
# |--|
# 5
#     |----|
# |--|
# В первом просто вставляем текущий и продолжаем искать позицию.
# В пятом мы можем вставить новый и затем присоединить все оставшиеся
# Остальных же мы должны слить два интервала. При этом пока не добавлять их,
# а представить их как новый, так как следующие могут тоже сливаться.

from typing import List

class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans = []
        new_st, new_end = newInterval
        for i, interval in enumerate(intervals):
            curr_st, curr_end = interval
            # 1
            if curr_end < new_st:
                ans.append([curr_st, curr_end])
            # 5
            elif new_end < curr_st:
                ans.append([new_st, new_end])
                ans += intervals[i:]
                break
            # 2,3,4
            else:
                new_st = min(new_st, curr_st)
                new_end = max(new_end, curr_end)
        else:
            ans.append([new_st, new_end])
        return ans


sol = Solution()
cases = [
    (([[1,3],[4,5],[6,6]], [2,3]), [[1,3],[4,5],[6,6]]),
    (([[1,3],[4,5],[6,6]], [2,4]), [[1,5],[6,6]]),
    (([[1,3],[4,5],[6,6]], [2,7]), [[1,7]]),
    (([[1,3],[4,5],[6,6]], [1,7]), [[1,7]]),
    (([[1,3],[4,5],[7,8]], [6,6]), [[1,3],[4,5],[6,6],[7,8]]),
    (([[1,3],[4,5],[7,8]], [6,6]), [[1,3],[4,5],[6,6],[7,8]]),
    (([], [1,2]), [[1,2]]),
    (([[1,3],[6,9]], [2,5]), [[1,5],[6,9]]),
    (([[1,3],[6,9]], [2,8]), [[1,9]]),
    (([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]]),
]
for inp, ans in cases:
    res = sol.insert(*inp)
    print(inp, res, ans)
