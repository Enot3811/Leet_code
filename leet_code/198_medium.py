"""House Rubber.

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight
without alerting the police.

 

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9)
and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12. 

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


from typing import List

    
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2


sol = Solution()
tests = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([5, 1, 6, 4, 2, 6, 1, 2, 8, 9], 28),
    ([3, 6, 6, 4, 9, 1], 18),
    ([94, 23, 33, 150, 39, 3, 46, 54, 27, 71, 12, 41, 64, 14, 82], 518),
    ([82, 94, 23, 1], 105),
    ([200, 275, 7, 305, 146, 9, 86, 371, 104, 192, 69, 254, 236, 143, 271, 238,
      202, 356, 274, 196, 157, 165, 375, 29, 89, 160, 130, 197, 390, 52, 151,
      11, 217, 349, 60, 313, 66, 160, 230, 46, 112, 349, 314, 285, 117, 216,
      353, 59, 119, 50, 364, 84, 256, 154, 244, 196, 131, 96, 338, 344, 91,
      142, 3, 209, 338, 57, 321, 329, 351, 174, 391, 169, 7, 153, 109, 127,
      300, 54, 362, 198, 304, 249, 192, 136, 34, 75, 333, 337, 388, 311, 50,
      38, 157, 184, 52, 107, 66, 60, 389, 122], 11150),
]

for inp, ans in tests:
    out = sol.rob(inp)
    print('Out:', out, 'Exp:', ans)
