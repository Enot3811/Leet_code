"""Longest Nice Subarray.

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements
that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice. 

Example 1:
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48].
This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example 2:
Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1.
Any subarray of length 1 can be chosen.

Constraints:
1 <= nums.length <= 10**5
1 <= nums[i] <= 10**9
"""

from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_len = 1
        # "And" текущего элемента с бинарным представлением "or" всех чисел
        # текущего nice subarray равноценно "and" со всеми её составляющими
        nice_sum = nums[0]
        for right in range(1, len(nums)):
            # Если текущее число подходит, то расширяем диапазон на 1 вправо
            # Если нет, то двигаем левую границу направо и удаляем старые
            # элементы до тех пор, пока "and" с текущим элементом не даст 0
            if nice_sum & nums[right] != 0:

                # Когда число не подошло, то длина будет уменьшаться.
                # Хороший момент, чтобы проверить максимум
                cur_len = right - left
                if cur_len > max_len:
                    max_len = cur_len
                
                # Одну итерацию пропускаем, так как текущую сумму уже проверили
                nice_sum ^= nums[left]
                left += 1
                
                # Двигаем левую границу
                while nice_sum & nums[right] != 0 and left != right:
                    nice_sum ^= nums[left]
                    left += 1

            # В любом случае, текущий элемент добавляем к диапазону
            nice_sum |= nums[right]
        
        # Проверить напоследок
        # +1 потому что в цикле right указывал на новый элемент,
        # а сейчас на границу nice subarray
        cur_len = right - left + 1
        if cur_len > max_len:
            max_len = cur_len
        return max_len


sol = Solution()
tests = [
    ([1,3,8,48,10], 3),
    ([3,1,5,11,13], 1),
    ([1, 2, 4, 8, 16, 32, 31, 1, 2, 4, 8, 16, 32, 64], 7),
    ([1, 2, 4, 8, 16, 32, 31, 1, 2, 4, 8, 16, 32, 64, 1], 7),
    ([1, 2, 4, 8, 16, 32, 31, 1, 2, 4, 8, 16, 32, 64, 1, 5], 7),
    ([0, 0, 0, 0, 9, 1, 2, 4, 8, 16], 5),
    ([0, 0, 0, 0, 9, 1, 2, 4, 8, 16, 32], 6),
    ([0, 0, 0, 0, 0, 9, 1, 2, 4, 8, 16, 32], 6),
    ([0, 0, 0, 0, 0, 0, 9, 1, 2, 4, 8, 16, 32], 7),
    ([0, 0, 0, 0, 9, 1, 2, 4, 8, 16, 15], 5),
    ([0, 0, 0, 0, 9, 1, 2, 4, 8, 16, 32, 15], 6),
    ([0, 0, 0, 0, 0, 0, 9, 1, 2, 4, 8, 16, 32, 15], 7),
    ([84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680], 8),
    ([1, 2, 4, 8, 3, 16, 32, 64], 6),
    ([1], 1)
]
for inp, ans in tests:
    print('Got:', sol.longestNiceSubarray(inp), 'Exp:', ans)
