"""81. Search in Rotated Sorted Array II

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order
(not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index
k (0 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated
at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000
-10**4 <= nums[i] <= 10**4
nums is guaranteed to be rotated at some pivot.
-10**4 <= target <= 10**4
"""

# Теги
# Бинарный поиск (binary search), Продолжение задачи

# Размышления
# Почти точная копия задачи (33. Search in Rotated Sorted Array).
# Отличие лишь в дубликатах, которые мешают определить упорядоченность половин.
# Например, 1,0,1,1,1. Что в левой 1 и 1, что в правой 1 и 1.
# Непонятно, в какой половине искать.
# Какого-то умного трюка не оказалось,
# от дубликатов приходится избавляться в линейном режиме.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True

            # Отсекаем дубликаты, так как они не позволят определить упорядоченность
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            # Левая часть упорядочена
            if nums[left] <= nums[mid]:
                # Содержит target, ищем в ней
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Иначе он может быть только в правой
                else:
                    left = mid + 1
            # Правая часть упорядочена
            else:
                # Содержит target, ищем в ней
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Иначе он может быть только в левой
                else:
                    right = mid - 1
        return False

cases = [
    (([6,7,1,2,3,4,5], 6), True),
    (([6,7,1,2,3,4,5], 2), True),
    (([6,7,1,2,3,4,5], 7), True),
    (([6,7,1,2,3,4,5], 5), True),
    (([6,7,1,2,3,4,5], 4), True),
    (([1,2,4,4,4,4,6,8,9,9], 8), True),
    (([4,4,4,6,8,9,9,1,2,4], 8), True),
    (([4,4,4,6,8,9,9,1,2,4], 5), False),
    (([4,4,4,6,8,9,9,1,2,4], 3), False),
    (([4,4,4,6,8,9,9,1,2,4], 10), False),
    (([1], 1), True),
    (([1], 0), False),
    (([1,0,1,1,1], 0), True)
]
sol = Solution()
for inp, ans in cases:
    res = sol.search(*inp)
    print(inp, res, ans)
