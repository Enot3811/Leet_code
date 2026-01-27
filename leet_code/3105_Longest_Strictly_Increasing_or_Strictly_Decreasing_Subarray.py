"""3105. Longest Strictly Increasing or Strictly Decreasing Subarray

https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

You are given an array of integers nums.
Return the length of the longest subarray of nums which is either strictly increasing
or strictly decreasing.

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
Hence, we return 3.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50
"""

# Теги
# Просто лёгкая задача (Easy task)

# Размышления
# Просто идём по массиву и смотрим, число больше предыдущего или меньше,
# и так определяем, возрастающая сейчас последовательность или убывающая.
# Вся сложность в том, чтобы как-то лаконично это реализовать,
# не закапываться в кучу флагов.

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        max_dec = 1
        max_inc = 1
        dec = 1
        inc = 1
        for num in nums:
            # Убывающая продолжается/прерывается
            if num < prev:
                dec += 1
            else:
                max_dec = max(max_dec, dec)
                dec = 1
            # Возрастающая продолжается/прерывается
            if num > prev:
                inc += 1
            else:
                max_inc = max(max_inc, inc)
                inc = 1
            prev = num
        # Максимальные ранее и текущая
        return max(max_inc, max_dec, dec, inc)

cases = [
    ([1,4,3,3,2], 2),
    ([3,3,3,3], 1),
    ([3,2,1], 3),
    ([1,2,3,2,1], 3),
    ([1,2,3,4,2,1], 4),
    ([1,2,1,2,1,2,1], 2),
    ([1,1,1,1,1,1,2,1,1,1], 2)
]
sol = Solution()
for nums, ans in cases:
    res = sol.longestMonotonicSubarray(nums)
    print(nums, res, ans)
