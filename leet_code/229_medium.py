"""Majority Element II."""

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) / 3
        cnt = Counter(nums)
        return [key for key in cnt if cnt[key] > maj]
        

sol = Solution()
tests = [
    [3, 2, 3],
    [1],
    [1, 2],
    [1, 1, 2, 2, 3]
]

for test in tests:
    print(sol.majorityElement(test))
        