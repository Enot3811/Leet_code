"""Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in
the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2,
[1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4,
[0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_len = 0
        cur_len = 0
        prev_len = 0
        found_zero = False

        for i in range(len(nums)):
            if nums[i] == 1:
                cur_len += 1
            else:
                # Если дошли до нуля
                # то надо отметить, что он вообще существует
                found_zero = True

                # Если есть две слившиеся последовательности
                if cur_len != 0 and prev_len != 0:
                    max_len = max(cur_len + prev_len, max_len)
                    prev_len = cur_len
                    cur_len = 0

                # Если только одна текущая последовательность
                elif cur_len != 0:
                    prev_len = cur_len
                    cur_len = 0

                # Если ранее была какая-то последовательность за нулём,
                # но новую не насчитали
                elif prev_len != 0:
                    max_len = max(prev_len, max_len)
                    prev_len = 0

        # Если дошли до конца, то следует подвести результаты
        max_len = max(cur_len + prev_len, max_len)

        # Если не встретили ни одного нуля, то значит единицы это и есть вся
        # посчитанная последовательность. Удаляем один символ
        if not found_zero:
            max_len -= 1

        return max_len
