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
    

sol = Solution()
nums = [1, 1, 2]
print(sol.permuteUnique(nums))
