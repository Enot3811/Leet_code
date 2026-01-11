"""1493. Longest Subarray of 1's After Deleting One Element

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

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

# Теги
# Плавающее окно (left-right pointers)

# Размышления
# Задача относится к плавающему окну, но её можно ловко решить с двумя суммами
# - текущей и предыдущей, просто итерируясь по массиву.
# Если текущий элемент 1, то увеличиваем текущую длину на 1.
# Если 0, то в этот момент мы можем проверить предыдущую и текущую последовательности,
# которые ранее были связаны нулем.
# Предыдущая последовательность становится текущей, а текущую сбрасываем в ноль.
# Если предыдущей последовательности не было, или если она дальше, чем через 1 ноль,
# то предыдущая как раз будет равна 0 в итоге этой операции.
# Стоит также отметить, что в массиве может вообще не быть нулей.
# Тогда придётся удалить одну единицу.

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        ans = 0
        cur_len = 0
        prev_len = 0
        found_zero = False
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_len += 1
            else:
                found_zero = True
                ans = max(ans, cur_len + prev_len)
                prev_len = cur_len
                cur_len = 0
        ans = max(ans, cur_len + prev_len)
        if not found_zero:
            ans -= 1
        return ans

cases = [
    ([1,1,1,0,0], 3),
    ([1,1,1,0,1], 4),
    ([1,1,1,0,1,0,1,1,1,1], 5),
    ([0,0,1,1,1,0,1,0,1,1,1,1], 5),
    ([0,1,1,1,0,1,0,1,1,1,1], 5),
    ([1,1,1], 2),
    ([1], 0),
    ([1, 0], 1),
    ([0, 0], 0),
]
sol = Solution()
for nums, ans in cases:
    res = sol.longestSubarray(nums)
    print(nums, res, ans)
