"""Search in Rotated Sorted Array II.

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


from typing import List


# Решение не оптимально
# Можно начать бинарный поиск не находя стык
# Обходить неудобные массивы можно смешиванием этого с линейным поиском
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def linear_search(nums: List[int], target: int) -> bool:
            if target > first:
                for i in range(1, len(nums) - 1):
                    if nums[i] == target:
                        return True
                    if nums[i] > target:
                        return False
                    if nums[i] < first:
                        return False
            elif target < last:
                for i in range(len(nums) - 2, 0, -1):
                    if nums[i] == target:
                        return True
                    if nums[i] < target:
                        return False
                    if nums[i] > first:
                        return False
            return False

        def log_search(nums: List[int], target: int) -> bool:
            def bound_search(nums: List[int], left: int, right: int) -> int:
                length = right - left + 1
                mid_idx = (length - 1) // 2 + left
                mid = nums[mid_idx]
                first = nums[0]
                last = nums[-1]

                if length == 1:
                    return mid_idx

                # Условие стыка
                if mid <= last and mid <= first and nums[mid_idx - 1] > mid:
                    return mid_idx

                if mid <= first and mid <= last:
                    right = mid_idx - 1
                    return bound_search(nums, left, right)

                if mid >= first and mid >= last:
                    left = mid_idx + 1
                    return bound_search(nums, left, right)

                else:
                    raise

            def binary_search(nums: List[int], target: int, left, right):
                if left > right:
                    return False
                else:
                    mid = (left + right) // 2
                    if target == nums[mid]:
                        return True
                    elif target > nums[mid]:
                        return binary_search(nums, target, mid + 1, right)
                    else:
                        return binary_search(nums, target, left, mid - 1)
            
            right_bound_idx = bound_search(nums, 0, len(nums) - 1)
            left_bound_idx = right_bound_idx - 1
            left_bound = nums[left_bound_idx]
            right_bound = nums[right_bound_idx]

            if target == left_bound or target == right_bound:
                return True
            if target > left_bound:
                return False
            if target < right_bound:
                return False
            if target > last and target < left_bound:
                return binary_search(
                    nums[:right_bound_idx], target, 0, left_bound_idx)
            if target < first and target > right_bound:
                return binary_search(
                    nums[right_bound_idx:], target, 0,
                    len(nums) - right_bound_idx - 1)
            else:
                return False

        first = nums[0]
        last = nums[-1]
        if target == first or target == last:
            return True

        if first <= last:
            return linear_search(nums, target)
        else:
            return log_search(nums, target)

# Линейное решение
# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         first = nums[0]
#         last = nums[-1]
#         if target == first or target == last:
#             return True
#         if target > first:
#             for i in range(1, len(nums) - 1):
#                 if nums[i] == target:
#                     return True
#                 if nums[i] > target:
#                     return False
#                 if nums[i] < first:
#                     return False
#         elif target < last:
#             for i in range(len(nums) - 2, 0, -1):
#                 if nums[i] == target:
#                     return True
#                 if nums[i] < target:
#                     return False
#                 if nums[i] > first:
#                     return False
#         return False


sol = Solution()
tests = [([1, 1, 1, 1, 1, 1, 1], 1),
         ([1, 1, 1, 1, 1, 1, 1], 2),
         ([1, 1, 2, 3, 1, 1, 1, 1], 3),
         ([1, 1, 2, 3, 1, 1, 1, 1], 4),
         ([9, 9, 9, 9, 9, 1, 1], 1),
         ([9, 9, 9, 9, 9, 1, 1], 9),
         ([4, 5, 6, 1, 2, 3], 6),
         ([4, 5, 6, 4, 4, 4, 4], 6)]

tests += [([1, 2, 3, 1], 2),
          ([6], 0),
          ([6], 6),
          ([5, 5, 6, 1], 6),
          ([7, 7, 7, 6], 6),
          ([7, 7, 7, 5, 6, 7], 6)]

tests += [
    ([3, 4, 5, 1, 2, 2], 5),
    ([2, 2, 2, 2, 2, 2, 1], 2),
    ([2, 1, 1, 1, 1, 1, 1], 1),
    ([3, 3, 3, 2, 2], 3),
    ([3, 4, 5, 1, 1, 1, 1], 5),
    ([6, 6, 6, 6, 8, 1, 2, 2, 2, 4, 4], 5),
    ([3, 4, 5, 6, 8, 1, 2, 2, 2, 2], 7),
    ([1, 3, 5], 0),
    ([3, 5, 1], 5),
    ([5, 1, 3], 1)
]

for nums, target in tests:
    answer = sol.search(nums, target)
    print(answer)
