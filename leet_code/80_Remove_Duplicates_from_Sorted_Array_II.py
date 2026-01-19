"""80. Remove Duplicates from Sorted Array II

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k
(hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements
of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond
the returned k (hence they are underscores).

Constraints:
1 <= nums.length <= 3 * 10**4
-10**4 <= nums[i] <= 10**4
nums is sorted in non-decreasing order.
"""

# Теги
# Два указателя (read/write pointers)

# Размышления
# Проходим по строке, выявляя дубли.
# При этом храним указатель на место вставки.
# В итоге решение за O(n), где мы двигаем нужные элементы (только 2 на каждое число)
# на insert position, и игнорируем остальные

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 1
        double = False
        curr_num = nums[0]
        for i in range(1, len(nums)):
            # Число повторилось и дубля ещё не было.
            # Если дубль был, то просто скипаем
            if nums[i] == curr_num:
                if not double:
                    nums[insert_idx] = nums[i]
                    double = True
                    insert_idx += 1
            # Встречаем новое число
            else:
                # Запоминаем его, ждём дубль, делаем вставку
                curr_num = nums[i]
                nums[insert_idx] = curr_num
                double = False
                insert_idx += 1
        return insert_idx

# Второе решение хуже по асимптотике, но лучше как по скорости, так и по памяти
# из-за эффективности реализации Counter на си

from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers = Counter(nums)
        i = 0
        for number, count in numbers.items():
            cur_count = min(count, 2)
            nums[i:i + cur_count] = [number] * cur_count
            i += cur_count
        return i


cases = [
    ([1,1,1,2,2,3], 5),
    ([1,2,3,4], 4),
    ([1,1,2,2,3,3,4,4], 8),
    ([1,1,2,2,3,3,4,4,5], 9),
    ([1,1,2,2,3,4,4,5], 8),
    ([1,1,1,1,2,4,4,4,7,7,9], 8),
    ([1], 1),
]
sol = Solution()
for nums, ans in cases:
    inp = nums.copy()
    res = sol.removeDuplicates(nums)
    print(inp, nums[:res], res, ans)
