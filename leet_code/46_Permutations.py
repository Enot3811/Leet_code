"""Permutations.

Given an array nums of distinct integers,
return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_step(nums: List[int]):
            if len(nums) == 1:
                return [nums]
            
            inserter = nums[0]
            sum_permutes = permute_step(nums[1:])

            permutes = []
            for term in sum_permutes:
                for i in range(len(term) + 1):
                    permutes.append(term[:i] + [inserter] + term[i:])
            return permutes

        return permute_step(nums)


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.permute(nums))
