"""Search Insert Position."""


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                break
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        if nums[middle] < target:
            middle += 1
        return middle
