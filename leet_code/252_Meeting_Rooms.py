"""252. Meeting Rooms

Premium lock.
https://neetcode.io/problems/meeting-schedule/

Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

# Размышления
# В задачах на интервалы всегда будет полезно отсортировать их.
# После этого мы можем по порядку пройти по ним и проверять, что каждый следующий
# не касается предыдущего.
# То есть, что его начало расположено после конца предыдущего.

from typing import List, Tuple

class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int, int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        bound = 0
        for interval in intervals:
            if interval[0] < bound:
                return False
            bound = interval[1]
        return True


cases = [
    ([(0,30),(5,10),(15,20)], False),
    ([(5,8),(9,15)], True),
    ([(0,4),(6,9),(20,22),(5,5),(9,9),(9,15)], True),
    ([(0,4),(6,9),(20,22),(5,5),(9,10),(9,15)], False)
]
sol = Solution()
for intervals, ans in cases:
    res = sol.canAttendMeetings(intervals)
    print(intervals, res, ans)
