"""Permutations II.

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order. 

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute_step(nums: List[int]):
            if len(nums) == 1:
                return (nums,)
            
            inserter = nums[0]
            sum_permutes = tuple(permute_step(nums[1:]))

            permutes = set()
            for term in sum_permutes:
                for i in range(len(term) + 1):
                    permutes.add(tuple(term[:i] + (inserter,) + term[i:]))
            return permutes

        return tuple(permute_step(tuple(nums)))
    

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 2]
    print(sol.permuteUnique(nums))
