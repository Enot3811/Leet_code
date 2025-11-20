"""55. Jump Game

https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length
at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10**4
0 <= nums[i] <= 10**5
"""


from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0


sol = Solution()
cases = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([4,0,0,0,0,2,1,3,4], False),
    ([1,5,2,3,5,7,2,1,9], True),
    ([3,0,1,1,1,2,0,4,0,0,5,2,0,1,3,0,0,5,0,0,4], True),
    ([3,0,1,1,1,2,0,4,0,0,5,2,0,1,3,0,0,0,0,0,4], False),
    ([3,0,1,1,1,2,0,4,0,6,2,1,0,1,3,0,0,5,0,0,4], True),
    ([1], True),
    ([0], True),
    ([0,0,0,0,0,10], False)
]
for nums, ans in cases:
    res = sol.canJump(nums)
    print(nums, res, ans)
