class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        calc = 0
        for n in nums:
            calc ^= n
        return calc
