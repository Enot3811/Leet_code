"""53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4

Follow up: If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.
"""

# Теги
# Кумулятивная сумма (cumulative sum)

# Размышления
# Сначала казалось, что можно как-то пристроить префиксные суммы, 
# но всё оказалось ещё проще.
# Префиксная сумма тащит за собой всю сумму, а нас она перестаёт интересовать,
# уже когда достигает нуля.
# Будем проходить по массива и суммировать числа. Если текущая сумма положительна, то
# продолжаем к ней прибавлять. Если же она достигает нуля, то бросаем её,
# ведь лучше уже будет начать заново.
# Если она положительна, но начинает снижаться, мы её ещё не бросаем, так как она
# ещё может вырасти, но засекаем максимум

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum


sol = Solution()
examples = [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1,2,3,4], 10),
    ([-10,2,3,4,-6,4,5,-20], 12),
    ([-10,4,-6,4,5,-20], 9),
    ([-1,-1,6,-1,-1], 6),
    ([0], 0),
    ([-2,-5,3,3,-6,2,-1,5,0],6),
    ([-2,-5,3,3,-6,2,-2,5,0],6),
    ([-2,-5,3,3,-6,2,-1,6,0],7),
    ([-2,-1],-1),
    ([-3,-2,-5,-1,-4],-1),
    ([-3,-2,0,-1,-4],0),
    ([-9,-7,3,-6,-9,-9,2,-6,-7,4,-9],4)
]
for nums, ans in examples:
    res = sol.maxSubArray(nums)
    print(nums, res, ans)
