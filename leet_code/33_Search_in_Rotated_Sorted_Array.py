"""33. Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated
at an unknown index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices
and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10**4 <= nums[i] <= 10**4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10**4 <= target <= 10**4
"""

# Теги
# Бинарный поиск (binary search), Продолжение задачи

# Размышления
# Задача связана с 153 таской, где был такой же массив, но искали минимум, а не target.
# Берём половину массива. Она будет либо отсортированной (start < end), либо содержать
# разрыв (end < start).
# Если отсортирована, то мы как в обычном бинарном поиске можем посмотреть, находится
# ли target внутри диапазона, и делить пополам.
# Если же он не внутри диапазона, то он всё ещё может быть внутри половины с разрывом.
# Может быть, что обе половины окажутся отсортированными, если мы так удачно поделим.
# Тогда логика всё та же. Смотрим, входит ли в диапазон.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Левая половина отсортирована
            if nums[left] <= nums[mid]:
                # И target в её диапазоне
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Иначе он ещё может быть в правой
                else:
                    left = mid + 1
            # Если не отсортирована, то правая точно отсортирована
            else:
                # И target в её диапазоне
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Иначе target всё ещё может быть в левой
                else:
                    right = mid - 1
        return -1


sol = Solution()

examples = [
    (([4, 5, 1, 2, 3], 4), 0),
    (([4, 5, 1, 2, 3], 3), 4),
    (([4, 5, 1, 2, 3], 1), 2),
    (([1,2,3,4,5], 2), 1),
    (([5,6,7,1,2,3,4], 2), 4),
    (([5,6,7,1,2,3,4], 0), -1),
    (([5,6,7,1,2,3,4], 9), -1),
    (([1], 1), 0),
    (([1], 2), -1),
    (([7,8,9,1,2,3,4,5,6], 8), 1),
    (([7,8,9,1,2,3,4,5,6], 5), 7),
    (([7,8,9,1,2,3,4,5,6], -1), -1),
    (([7,8,9,1,2,3,4,5,6], 10), -1),
    (([4,5,6,7,0,1,2], 0), 4),
    (([4,5,6,7,0,1,2], 3), -1)
]
for inp, ans in examples:
    res = sol.search(*inp)
    print(inp, res, ans)