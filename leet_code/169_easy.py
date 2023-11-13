"""Majority Element."""

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max(cnt, key=lambda k: cnt[k])


sol = Solution()
tests = [
    [2,2,1,1,1,2,2],
    [1, 2, 3, 3, 3],
    [1],
    [1, 1],
    [1, 2, 3, 4, 3, 2, 1, 4, 4, 4, 4, 4, 4]
]

for test in tests:
    print(sol.majorityElement(test))
        