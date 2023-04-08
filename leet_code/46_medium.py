"""Permutations."""


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


nums = [1, 2, 3]
sol = Solution()
print(sol.permute(nums))
