"""Maximum Gap."""


from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        gap = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff > gap:
                gap = diff
        return gap

sol = Solution()
tests = [
    ([3,6,9,1], 3),
    ([10], 0),
    ([5, 10, 9, 1, 11, 13, 5, 20], 7),
    ([1, 1, 1, 1, 1], 0)
]
for inp, ans in tests:
    out = sol.maximumGap(inp)
    print('Out:', out, 'Exp:', ans)
