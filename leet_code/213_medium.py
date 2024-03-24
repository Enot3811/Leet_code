"""House Rubber II.

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight
without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2)
and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.solve(nums[1:]), self.solve(nums[:-1]))

    def solve(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2



sol = Solution()
tests = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([5, 1, 6, 4, 2, 6, 1, 2, 8, 9], 25),
    ([3, 6, 6, 4, 9, 1], 18),
    ([943, 231, 331, 981, 398, 3, 463, 547, 276, 713, 129, 414, 642, 147, 827,
      852, 950, 887, 399, 629, 403, 12, 505, 644, 685, 633, 777, 357, 70, 543,
      115, 882, 912, 85, 237, 876, 556, 502, 426, 699, 885, 372, 668, 99, 897,
      209, 388, 186, 101, 738, 990, 577, 583, 108, 736, 313, 820, 14, 740, 49,
      801, 892, 941, 263, 597, 734, 517, 223, 939, 325, 269, 256, 611, 401,
      493, 968, 396, 861, 398, 993, 730, 655, 504, 309, 601, 360, 775, 320,
      487, 223, 973, 356, 383, 45, 247, 32, 153, 491, 351, 586], 30193),
    ([907, 486, 75, 602, 431, 822, 656, 108, 822, 624, 661, 869, 122, 76, 624,
      705, 187, 873, 445, 54], 5676),
    ([943, 231, 331, 981, 398, 3, 463, 547, 276, 713, 129, 414, 642, 147, 827,
      852, 950, 887, 399, 629, 403, 12, 505, 644, 685, 633, 777, 357, 70, 543,
      115, 882, 912, 85, 237, 876, 556, 502, 426, 699, 885, 372, 668, 99, 897,
      209, 388, 186, 101, 738, 990, 577, 583, 108, 736, 313, 820, 14, 740, 49],
      18071),
    ([94, 23, 33, 98, 39, 3, 46, 54, 27, 71, 12, 41, 64, 14, 82], 395),
    ([82, 94, 23, 1], 105),
    ([1], 1)
]
for inp, ans in tests:
    out = sol.rob(inp)
    print('Out:', out, 'Exp:', ans)
