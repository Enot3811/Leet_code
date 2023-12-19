"""Majority Element.

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10**4
-10**9 <= nums[i] <= 10**9
"""

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
        