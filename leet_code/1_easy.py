'''Two sum.'''


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [i, seen[diff]]
            seen[num] = i


sol = Solution()
nums = [2, 7, 10, 4]
target = 17
print(sol.twoSum(nums, 17))
