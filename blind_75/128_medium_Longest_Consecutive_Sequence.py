"""128. Longest Consecutive Sequence

https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
"""


# Размышления
# Не очень интуитивная идея, которую я подсмотрел
# Конвертируем в сет массив, и затем благодаря быстрой проверке на наличие элементов
# мы можем смотреть, есть ли у n-го числа сосед слева. Так определим, является ли он
# началом какой-то из последовательностей.
# А затем можем так же делать проверки и вправо, чтобы выделить его последовательность

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_seq_len = 0
        for num in set_nums:
            # Если нет соседа слева, то это начальное число последовательности
            if num - 1 not in set_nums:
                cur_seq_len = 1
                # Проверяем правых соседей,
                # чтобы определить длинную этой последовательности
                while num + 1 in set_nums:
                    num += 1
                    cur_seq_len += 1
                max_seq_len = max(max_seq_len, cur_seq_len)
        return max_seq_len


sol = Solution()

examples = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([1, 0, 1, 2], 3),
    ([1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, -1, 0], 5),
    ([], 0),
    ([1], 1),
    ([1, 1, 1, 1], 1)
]
for nums, ans in examples:
    res = sol.longestConsecutive(nums)
    print(nums, res, ans)