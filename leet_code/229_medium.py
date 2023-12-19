"""Majority Element II.

Given an integer array of size n,
find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 10**4
-10**9 <= nums[i] <= 10**9
"""

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
        