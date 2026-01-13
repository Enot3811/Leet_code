"""283. Move Zeroes

https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""

# Теги
# Два указателя (read/write pointers)

# Размышления
# Будем сдвигать числа начиная с нулевого индекса, затирая нули.
# При этом посчитаем, сколько их было, чтобы после вставить их в конец.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0
        cur_idx = 0
        for i, num in enumerate(nums):
            if num == 0:
                zero_counter += 1
            else:
                if cur_idx != i:
                    nums[cur_idx] = num
                cur_idx += 1
        for i in range(len(nums) - 1, len(nums) - 1 - zero_counter, -1):
            nums[i] = 0


sol = Solution()
examples = [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([1,2,3,4], [1,2,3,4]),
    ([0,0,0,0], [0,0,0,0]),
    ([1], [1]),
    ([1,0,3,12], [1,3,12,0])
]

for inp, ans in examples:
    redacted = inp.copy()
    sol.moveZeroes(redacted)
    print(inp, redacted, ans)
