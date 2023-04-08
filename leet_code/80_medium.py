'''Remove Duplicates from Sorted Array II.'''


from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers = Counter(nums)
        i = 0
        for number, count in numbers.items():
            cur_count = min(count, 2)
            nums[i:i + cur_count] = [number] * cur_count
            i += cur_count
        return i


sol = Solution()
nums = [0, 1, 2, 3]
print(sol.removeDuplicates(nums))
print(nums)
